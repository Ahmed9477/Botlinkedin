
"""
LinkedIn Auto Poster 🤖
- Génération de posts LinkedIn via IA
- Hashtags intelligents multi-thèmes
- Pilotage via Google Sheets
- Publication automatique 2x/semaine
"""

import os
import re
import time
import requests
import schedule
import gspread

from datetime import datetime
from openai import OpenAI
from google.oauth2.service_account import Credentials


# =========================
# 🔐 VARIABLES D'ENVIRONNEMENT
# =========================

LINKEDIN_TOKEN = os.getenv("LINKEDIN_TOKEN")
LINKEDIN_PERSON_URN = os.getenv("LINKEDIN_PERSON_URN")
LINKEDIN_PERSON_ID = os.getenv("LINKEDIN_PERSON_ID")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME", "LinkedInPosts")

GOOGLE_CREDS_FILE = os.getenv("GOOGLE_CREDS_FILE", "creds.json")

if not all([
    LINKEDIN_TOKEN,
    LINKEDIN_PERSON_URN,
    LINKEDIN_PERSON_ID,
    OPENAI_API_KEY
]):
    raise EnvironmentError("❌ Variables d'environnement manquantes")


# =========================
# 🔗 CLIENTS & CONFIG
# =========================

headers_api = {
    "Authorization": f"Bearer {LINKEDIN_TOKEN}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0.0",
    "LinkedIn-Version": "202501"
}

client_openai = OpenAI(api_key=OPENAI_API_KEY)

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(GOOGLE_CREDS_FILE, scopes=scope)
gspread_client = gspread.authorize(creds)
sheet = gspread_client.open(GOOGLE_SHEET_NAME).sheet1


# =========================
# ✍️ IA – GÉNÉRATION POST
# =========================

def generate_post(theme, angle=""):
    """
    Génère un post LinkedIn en français via OpenAI
    """
    prompt = f"""
Post LinkedIn français naturel ~200 mots.

Thème : {theme}
Angle : {angle}

Structure :
- Question d'accroche
- Expérience personnelle
- 💡 2 conseils concrets
- Question finale

Ne mets PAS les hashtags.
"""

    try:
        response = client_openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.75
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return f"🚀 {theme}\n\nMon expérience...\n\nVotre avis ? 👇"


def generate_hashtags(text, theme):
    """
    Génère 4 hashtags LinkedIn pertinents
    """
    prompt = f"""
Génère EXACTEMENT 4 hashtags LinkedIn français pertinents
à partir de ce texte :

\"\"\"{text[:300]}\"\"\"

Thème principal : {theme}

Format :
#MotCle1 #MotCle2 #MotCle3 #LinkedIn
"""

    try:
        response = client_openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=60,
            temperature=0.3
        )
        hashtags = response.choices[0].message.content.strip()
        return re.sub(r"[^#A-Za-zÀ-ÿ\s]", "", hashtags)
    except Exception:
        return "#LinkedIn #Experience #Business #IA"


def perfect_post(raw_text, theme):
    """
    Nettoie, formate et ajoute les hashtags
    """
    text = re.sub(r"[*`]", "", raw_text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    if not text.startswith("🚀"):
        text = "🚀 " + text

    if "👇" not in text:
        text += "\n\n👇"

    hashtags = generate_hashtags(text, theme)
    text += f"\n\n{hashtags}"

    return text[:2900]


# =========================
# 🚀 PUBLICATION LINKEDIN
# =========================

def post_linkedin():
    """
    Publie le premier post marqué 'OUI' dans Google Sheets
    """
    try:
        records = sheet.get_all_records()
        headers = sheet.row_values(1)
        header_idx = {h: i + 1 for i, h in enumerate(headers)}

        for row_idx, row in enumerate(records, start=2):

            row_text = " ".join(str(v).lower() for v in row.values())
            if "oui" not in row_text:
                continue

            theme = row.get("Thème") or row.get("Theme") or "Expérience"
            angle = row.get("Angle", "")

            raw_post = generate_post(theme, angle)
            final_post = perfect_post(raw_post, theme)

            data = {
                "author": LINKEDIN_PERSON_URN,
                "lifecycleState": "PUBLISHED",
                "specificContent": {
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {"text": final_post},
                        "shareMediaCategory": "NONE"
                    }
                },
                "visibility": {
                    "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
                }
            }

            r = requests.post(
                "https://api.linkedin.com/v2/ugcPosts",
                headers=headers_api,
                json=data
            )

            if r.status_code == 201:
                post_id = r.json()["id"]
                post_url = f"https://www.linkedin.com/posts/{LINKEDIN_PERSON_ID}_{post_id}"

                sheet.update_cell(row_idx, header_idx["Validité"], "NON")
                sheet.update_cell(
                    row_idx,
                    header_idx["Post généré"],
                    f'=HYPERLINK("{post_url}", "✅ POSTÉ {datetime.now().strftime("%H:%M")}")'
                )

                print(f"✅ Post publié : {post_url}")
                return True

            print(f"❌ Erreur LinkedIn : {r.status_code}")
            return False

        print("ℹ️ Aucun post marqué OUI")
        return False

    except Exception as e:
        print(f"💥 Erreur : {e}")
        return False


# =========================
# ⏰ PLANIFICATION
# =========================

schedule.every().monday.at("09:00").do(post_linkedin)
schedule.every().thursday.at("09:00").do(post_linkedin)

print("🤖 LinkedIn Auto Poster lancé")

post_linkedin()

while True:
    schedule.run_pending()
    time.sleep(3600)

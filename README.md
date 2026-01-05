# 🤖 LinkedIn Auto Poster (AI-powered)

Automatisation complète de publications LinkedIn avec génération de contenu par intelligence artificielle et planification hebdomadaire.

Ce bot permet de publier automatiquement **2 posts par semaine** à partir de thèmes définis dans Google Sheets, avec **hashtags intelligents** adaptés au contenu (business, IA, sport, lifestyle, etc.).

---

## 🚀 Fonctionnalités

- Génération automatique de posts LinkedIn en français via IA
- Hashtags intelligents basés sur le contenu réel du post
- Pilotage simple via Google Sheets
- Publication automatique via l’API LinkedIn (UGC)
- Planification hebdomadaire (lundi & jeudi)
- Historique des posts avec lien cliquable
- Aucun secret exposé (variables d’environnement)

---

## 🧠 Stack technique

- **Python 3.10+**
- **OpenAI API**
- **LinkedIn UGC API**
- **Google Sheets API**
- gspread
- schedule
- requests

---

## 📁 Structure du projet

```text
linkedin-auto-poster/
│
├── bot_linkedin.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── credentials/
    └── creds.json.example
```
# ⚙️ Installation
## 1️⃣ Cloner le dépôt

git clone https://github.com/your-username/linkedin-auto-poster.git
cd linkedin-auto-poster

## 2️⃣ Installer les dépendances

pip install -r requirements.txt

# 🔐 Configuration
## 1️⃣ Variables d’environnement

```Créer un fichier .env à partir de .env.example :

LINKEDIN_TOKEN=your_linkedin_token
LINKEDIN_PERSON_URN=urn:li:person:XXXX
LINKEDIN_PERSON_ID=XXXX

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx

GOOGLE_SHEET_NAME=LinkedInPosts
GOOGLE_CREDS_FILE=creds.json
```
## 2️⃣ Google Sheets

Créer un Google Sheet avec les colonnes suivantes :

Colonne	     --->             Description
Thème	        --->           Sujet du post
Angle	        --->     Angle ou point de vue (optionnel)
Validité	    --->    Mettre OUI pour autoriser la publication
Post généré    --->    Lien du post publié automatiquement

## 3️⃣ Google Service Account

-Créer un service account Google
-Télécharger le fichier creds.json
-Le placer localement (jamais sur GitHub)
-Utiliser creds.json.example comme modèle

# ▶️ Lancement du bot

```bash
python bot_linkedin.py
```
#Le bot :

-détecte le premier post marqué OUI
-génère automatiquement le contenu + les hashtags
-publie le post sur LinkedIn
-met à jour la Google Sheet (lien cliquable)
-reste actif en continu (scheduler)

# ⏰ Planning par défaut

-📅 Lundi à 09:00
-📅 Jeudi à 09:00

Ces horaires sont modifiables directement dans le script.

# 🔒 Sécurité

Ce projet est conçu pour être 100 % safe GitHub :

-❌ Aucun token en dur dans le code
-❌ Aucune clé privée versionnée
-✅ Variables d’environnement uniquement
-✅ Fichiers .example fournis pour la configuration


# 📌 Cas d’usage

-Personal branding
-Créateurs de contenu
-Freelances / entrepreneurs
-Community management
-Automatisation marketing

🧑‍💻 Auteur

Ahmed Jaafar 



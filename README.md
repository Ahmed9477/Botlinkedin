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

| **Élément** | **Détails** |
|------------|-------------|
| **Nom du projet** | Indiquer le nom officiel du projet. |
| **Thème** | Préciser le thème ou le domaine principal du projet. |
| **Équipe** | Liste des personnes avec qui vous avez collaboré sur ce projet. |
| **Validation** | Indiquer si le projet a été validé ou approuvé (Oui / Non). |
| **Description du projet** | Fournir une description complète et concise du projet, expliquant ce qu’il fait et ses particularités. |
| **Objectif principal** | Décrire l’objectif principal ou la finalité du projet. |
| **Contexte** | Expliquer le contexte dans lequel le projet a été réalisé (cours, entreprise, recherche, etc.). |
| **Livrable** | Décrire le livrable attendus |


## 3️⃣ Google Service Account

- Créer un service account Google
- Télécharger le fichier creds.json
- Le placer localement (jamais sur GitHub)
- Utiliser creds.json.example comme modèle

## ▶️ Lancement du bot

```bash
python bot_linkedin.py
```
#Le bot :

- Détecte le premier post marqué **OUI**  
- Génère automatiquement le contenu et les hashtags  
- Publie le post sur **LinkedIn**  
- Met à jour la **Google Sheet** (lien cliquable)  
- Reste actif en continu via un **scheduler**  


## ⏰ Planning par défaut

- 📅 Lundi à 09:00
- 📅 Jeudi à 09:00

Ces horaires sont modifiables directement dans le script.

## 🔒 Sécurité

Ce projet est conçu pour être **100 % safe GitHub** :

- ❌ Aucun token en dur dans le code  
- ❌ Aucune clé privée versionnée  
- ✅ Utilisation exclusive de variables d’environnement  
- ✅ Fichiers `.example` fournis pour la configuration  


## 📌 Cas d’usage

- Personal branding  
- Créateurs de contenu  
- Freelances / entrepreneurs  
- Community management  
- Automatisation marketing  

🧑‍💻 Auteur

Ahmed Jaafar 



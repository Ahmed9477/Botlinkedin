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

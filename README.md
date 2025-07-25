# 🌐 sLworld

Le backend de sLworld développée avec [Flask](https://flask.palletsprojects.com/), un micro-framework Python.

---

## 📦 Prérequis

- Python 3.12 ou version ultérieure
- `pip`

---

## 🐍 Création et activation de l’environnement virtuel

### 1. Créer un environnement virtuel

```bash
python3 -m venv env
```

### 2. Activer l’environnement

- <details><summary>Linux / macOS :</summary>

```bash
source env/bin/activate
```
</details>

- <details><summary>Windows (cmd) :</summary>

```cmd
.\env\Scripts\activate
```
</details>

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

--- 

## Lancer le serveur Flask

```bash
python3 app.py
```

---

## Créer des bases de donées

```bash
mkdir databases
cd databases
touch User.db
```

Puis renter ce SQL dans `User.db`
```SQL
CREATE TABLE "Users" (
	"Id"	INTEGER,
	"Username"	TEXT,
	"Name"      TEXT,
	"Passworld"	TEXT,
	"Email"     TEXT,
	PRIMARY KEY("Id")
);
```

---

## 🧾 À ne pas oublier

Ajoutez env .gitignore

---

Made with ❤️ by Spider Lambo
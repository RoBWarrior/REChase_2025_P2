# 🕵️‍♂️ REChase-2025  
### *An Online Treasure Hunt Game*  

---

## 📘 Overview  

**REChase-2025** is a Django-based online treasure hunt platform designed for interactive and engaging gameplay.  
This guide walks you through setting up, running, and managing the project locally.

---

## 🚀 Quick Start  

If you just want to get the app running quickly, follow the commands below:

### 1️⃣ Create and Activate a Virtual Environment  

#### 🪟 Windows  
```bash
pip install virtualenv
virtualenv myenv
myenv\Scripts\activate
```

#### 🐧 Linux / macOS  
```bash
pip install virtualenv
virtualenv myenv
source myenv/bin/activate
```

**💡 Tip:** For detailed steps, see  
[Creating Python Virtual Environments (Windows/Linux)](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)

---

### 2️⃣ Install Dependencies and Set Up Environment Variables  
```bash
# Install all required Python packages
pip install -r requirements.txt

# Create a new .env file from the example template
cp .env.example .env
```

---

### 3️⃣ Initialize the Database  
```bash
# Make database migrations
python manage.py makemigrations

# Apply the migrations
python manage.py migrate

# Load initial data into the database
python manage.py loaddata du.json
```

---

### 4️⃣ Run the Development Server  
```bash
python manage.py runserver
```

Once the server starts, open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 📂 Data Management  

### 🔹 Export (Dump) Existing Data  

Use this command to export your database data (excluding Django’s default auth tables):

```bash
python manage.py dumpdata --exclude auth.permission --exclude contenttypes --indent 4 > {filename}.json
```

### 🔹 Import (Load) Existing Data  

Load data back into your database using:

```bash
python manage.py loaddata {filename}.json
```

> **Note:** Replace `{filename}` with your desired JSON file name.

---

## 💡 Helpful Tips  

- ✅ Always activate your **virtual environment** before running Django commands.  
- ⚙️ Customize your `.env` file according to your environment.  
- 🔁 To reset your database, delete `db.sqlite3` and rerun the **migration + loaddata** steps.  
- 🔐 You can create an admin user with:  

```bash
python manage.py createsuperuser
```

---

## 💻 Developed For  

🎯 **REChase-2025 — Online Treasure Hunt Event**  
An interactive coding and puzzle-solving experience for curious minds.

---

## 🧭 License  

This project is created for **event purposes only**.  
You are free to **modify and adapt** it for our own treasure hunts or internal events.

---

## 💬 Support  

If you face issues while setting up or running the project:

- 🔄 Recheck your **virtual environment activation**.  
- 📦 Ensure all dependencies from `requirements.txt` are installed.  
- ⚙️ Verify `.env` configuration values.  
- 🧱 Run migrations again if database errors occur.

---

## 🌟 Happy Hunting & Good Luck! 🌟

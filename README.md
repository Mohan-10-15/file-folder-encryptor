# 🔐 File Encryptor GUI

A simple and secure File & Folder Encryption tool built using Python.

This application allows users to:
- Encrypt individual files
- Decrypt encrypted files
- Encrypt entire folders
- Decrypt entire folders

It uses strong cryptographic encryption to protect your data.

---

## 🚀 Features

✔ Encrypt files securely  
✔ Decrypt files safely  
✔ Encrypt all files inside a folder  
✔ Decrypt all files inside a folder  
✔ Simple graphical user interface (GUI)  
✔ Easy to use  

---

## 🛠 Built With

- Python 3
- Tkinter (GUI)
- Cryptography (Fernet encryption)

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Mohan-10-15/file-encryptor.git
### 2️⃣ Navigate to project folder
```bash
cd file-encryptor
### 3️⃣ Install required package
```bash
pip install cryptography
▶️ How to Run
python file_encryptor_gui.py

The application window will open.

🔐 How It Works

The user selects a file or folder.

A password is provided.

The password is converted into a secure encryption key.

Files are encrypted using Fernet symmetric encryption.

Encrypted files can only be decrypted using the correct password.

⚠ Important Notes

If you forget the password, the encrypted data cannot be recovered.

Always keep your password safe.

Do not modify encrypted files manually.

📁 Project Structure
file-encryptor/
│
├── file_encryptor_gui.py
└── README.md
📜 License

This project is open-source and free to use.

👨‍💻 Author

Created by Mohan
GitHub: https://github.com/Mohan-10-15

Python Developer 🚀

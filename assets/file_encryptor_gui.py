import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import hashlib, base64, zipfile, os, shutil

# ---------- KEY ----------
def generate_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

# ---------- PASSWORD STRENGTH ----------
def check_strength(event=None):
    pwd = password.get()
    strength = "Weak"
    color = "red"
    if len(pwd) >= 12 and any(c.isdigit() for c in pwd) and any(c.isupper() for c in pwd):
        strength = "Strong"
        color = "green"
    elif len(pwd) >= 8:
        strength = "Medium"
        color = "orange"
    strength_label.config(text=f"Strength: {strength}", fg=color)

# ---------- FILE ENCRYPT ----------
def encrypt_file():
    path = filedialog.askopenfilename()
    if not path: return
    pwd = password.get()
    if not pwd: return error()

    f = Fernet(generate_key(pwd))
    data = open(path, "rb").read()
    enc = f.encrypt(data)

    with open(path + ".encrypted", "wb") as out:
        out.write(enc)

    if delete_original.get():
        os.remove(path)

    messagebox.showinfo("Done", "File encrypted")

# ---------- FILE DECRYPT ----------
def decrypt_file():
    path = filedialog.askopenfilename(filetypes=[("Encrypted", "*.encrypted")])
    if not path: return
    pwd = password.get()
    if not pwd: return error()

    try:
        f = Fernet(generate_key(pwd))
        data = open(path, "rb").read()
        dec = f.decrypt(data)

        out_path = path.replace(".encrypted", "")
        open(out_path, "wb").write(dec)
        messagebox.showinfo("Done", "File decrypted")
    except:
        messagebox.showerror("Error", "Wrong password")

# ---------- FOLDER ENCRYPT ----------
def encrypt_folder():
    folder = filedialog.askdirectory()
    if not folder: return
    pwd = password.get()
    if not pwd: return error()

    zip_path = folder + ".zip"
    shutil.make_archive(folder, "zip", folder)

    f = Fernet(generate_key(pwd))
    enc = f.encrypt(open(zip_path, "rb").read())

    open(folder + ".encrypted", "wb").write(enc)
    os.remove(zip_path)

    if delete_original.get():
        shutil.rmtree(folder)

    messagebox.showinfo("Done", "Folder encrypted")

# ---------- FOLDER DECRYPT ----------
def decrypt_folder():
    path = filedialog.askopenfilename(filetypes=[("Encrypted", "*.encrypted")])
    if not path: return
    pwd = password.get()
    if not pwd: return error()

    try:
        f = Fernet(generate_key(pwd))
        dec = f.decrypt(open(path, "rb").read())

        zip_path = path.replace(".encrypted", ".zip")
        open(zip_path, "wb").write(dec)

        out = zip_path.replace(".zip", "")
        with zipfile.ZipFile(zip_path) as z:
            z.extractall(out)

        os.remove(zip_path)
        messagebox.showinfo("Done", "Folder decrypted")
    except:
        messagebox.showerror("Error", "Wrong password")

def error():
    messagebox.showerror("Error", "Enter password")

# ---------- GUI ----------
root = tk.Tk()
root.title("File & Folder Encryptor")
root.geometry("450x420")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

tk.Label(root, text="Password", fg="white", bg="#1e1e1e").pack(pady=5)
password = tk.Entry(root, show="*", width=30)
password.pack()
password.bind("<KeyRelease>", check_strength)

strength_label = tk.Label(root, text="Strength: ", bg="#1e1e1e")
strength_label.pack(pady=4)

delete_original = tk.BooleanVar()
tk.Checkbutton(root, text="Delete original after encrypt",
               variable=delete_original, bg="#1e1e1e",
               fg="white", selectcolor="#1e1e1e").pack(pady=6)

btn = lambda t, c: tk.Button(root, text=t, width=28, command=c).pack(pady=6)

btn("Encrypt File", encrypt_file)
btn("Decrypt File", decrypt_file)
btn("Encrypt Folder", encrypt_folder)
btn("Decrypt Folder", decrypt_folder)

tk.Label(root, text="All-in-One Secure Encryptor", fg="gray", bg="#1e1e1e").pack(pady=10)

root.mainloop()
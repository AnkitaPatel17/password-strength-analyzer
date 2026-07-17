import tkinter as tk
from tkinter import ttk, messagebox
import re
import random
import string

# ---------------- Common Passwords ----------------

common_passwords = [
    "password", "123456", "123456789", "qwerty",
    "abc123", "admin", "welcome", "letmein"
]

# ---------------- Analyze Password ----------------

def analyze_password():
    password = entry_password.get()

    if not password:
        messagebox.showwarning("Warning", "Please enter a password.")
        return

    score = 0
    feedback = []

    # Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("• Password should contain at least 8 characters.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("• Add at least one uppercase letter.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("• Add at least one lowercase letter.")

    # Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("• Add at least one number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("• Add at least one special character.")

    # Common Password Check
    if password.lower() in common_passwords:
        score = max(score - 2, 0)
        feedback.append("• This password is too common.")

    # Determine Strength
    if score <= 2:
        strength = "Weak"
        color = "red"
        progress["value"] = 30
    elif score <= 4:
        strength = "Medium"
        color = "orange"
        progress["value"] = 65
    else:
        strength = "Strong"
        color = "green"
        progress["value"] = 100

    lbl_strength.config(text="Strength: " + strength, fg=color)

    txt_feedback.delete("1.0", tk.END)

    if feedback:
        txt_feedback.insert(tk.END, "\n".join(feedback))
    else:
        txt_feedback.insert(tk.END, "Excellent! Your password is strong.")

# ---------------- Generate Password ----------------

def generate_password():
    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        "!@#$%^&*?"
    )

    while True:
        password = "".join(random.choice(characters) for _ in range(16))

        if (re.search(r"[A-Z]", password) and
            re.search(r"[a-z]", password) and
            re.search(r"\d", password) and
            re.search(r"[!@#$%^&*?]", password)):
            break

    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

# ---------------- Show / Hide Password ----------------

def toggle_password():
    if show_var.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

# ---------------- Clear ----------------

def clear_all():
    entry_password.delete(0, tk.END)
    txt_feedback.delete("1.0", tk.END)
    lbl_strength.config(text="Strength:", fg="black")
    progress["value"] = 0

# ---------------- GUI ----------------

root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("550x500")
root.resizable(False, False)
root.configure(bg="#F4F6F8")

title = tk.Label(
    root,
    text="Password Strength Analyzer",
    font=("Arial", 18, "bold"),
    bg="#F4F6F8",
    fg="#003366"
)
title.pack(pady=15)

label = tk.Label(
    root,
    text="Enter Password",
    font=("Arial", 12),
    bg="#F4F6F8"
)
label.pack()

entry_password = tk.Entry(
    root,
    width=35,
    font=("Arial", 12),
    show="*"
)
entry_password.pack(pady=8)

show_var = tk.BooleanVar()

check = tk.Checkbutton(
    root,
    text="Show Password",
    variable=show_var,
    command=toggle_password,
    bg="#F4F6F8"
)
check.pack()

button_frame = tk.Frame(root, bg="#F4F6F8")
button_frame.pack(pady=15)

btn1 = tk.Button(
    button_frame,
    text="Analyze",
    width=15,
    bg="#28A745",
    fg="white",
    font=("Arial", 10, "bold"),
    command=analyze_password
)
btn1.grid(row=0, column=0, padx=5)

btn2 = tk.Button(
    button_frame,
    text="Generate Password",
    width=18,
    bg="#007BFF",
    fg="white",
    font=("Arial", 10, "bold"),
    command=generate_password
)
btn2.grid(row=0, column=1, padx=5)

btn3 = tk.Button(
    button_frame,
    text="Clear",
    width=10,
    bg="#DC3545",
    fg="white",
    font=("Arial", 10, "bold"),
    command=clear_all
)
btn3.grid(row=0, column=2, padx=5)

progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=350,
    mode="determinate"
)
progress.pack(pady=15)

lbl_strength = tk.Label(
    root,
    text="Strength:",
    font=("Arial", 14, "bold"),
    bg="#F4F6F8"
)
lbl_strength.pack()

suggestion = tk.Label(
    root,
    text="Suggestions",
    font=("Arial", 12, "bold"),
    bg="#F4F6F8"
)
suggestion.pack(pady=5)

txt_feedback = tk.Text(
    root,
    width=60,
    height=10,
    font=("Arial", 10)
)
txt_feedback.pack(pady=5)

root.mainloop()
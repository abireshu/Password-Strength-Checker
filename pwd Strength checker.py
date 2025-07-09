import tkinter as tk
from pwd_Scheck_code import pwd_checker

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x420")
root.configure(bg="#121212")
root.resizable(False, False)

header = tk.Label(
    root, text="🔐 Password Strength Checker", font=("Arial", 16, "bold"),
    bg="#121212", fg="#8EE81F"
)
header.pack(pady=20)

tk.Label(
    root, text="Enter your password:", font=("Arial", 12),
    bg="#121212", fg="white"
).pack(pady=5)

entry_frame = tk.Frame(root, bg="#121212")
entry_frame.pack()

entry = tk.Entry(entry_frame, show="*", width=30, font=("Arial", 12), relief=tk.GROOVE, bd=2)
entry.pack(side=tk.LEFT, padx=(0, 10))

show_var = tk.BooleanVar(value=False)

def toggle_password():
    if show_var.get():
        entry.config(show="")
    else:
        entry.config(show="*")

show_password = tk.Checkbutton(
    entry_frame, text="Show", variable=show_var, command=toggle_password,
    bg="#121212", fg="white", activebackground="#121212",
    activeforeground="white", selectcolor="#121212"
)
show_password.pack(side=tk.LEFT)

canvas = tk.Canvas(root, width=300, height=20, bg="#2D2B2B", highlightthickness=0)
canvas.pack(pady=25)
bar = canvas.create_rectangle(0, 0, 0, 20, fill="red", width=0)

def animate_bar(percent):
    width = 3 * percent
    canvas.coords(bar, 0, 0, width, 20)
    if percent < 40:
        color = "#FF4C4C"
    elif percent < 70:
        color = "#FFA500"
    else:
        color = "#8EE81F"
    canvas.itemconfig(bar, fill=color)

def check_password():
    password = entry.get()
    result, color, strength_percent = pwd_checker(password)
    result_label.config(text=result, fg=color)
    animate_bar(strength_percent)

check_btn = tk.Button(
    root, text="Check Strength", command=check_password,
    font=("Arial", 12, "bold"), bg="#1F1F1F", fg="#8EE81F",
    relief=tk.RAISED, bd=3, padx=10, pady=5
)
check_btn.pack(pady=10)

result_label = tk.Label(
    root, text="", font=("Arial", 12, "bold"),
    bg="#121212", fg="white", wraplength=450, justify="center"
)
result_label.pack(pady=10)

root.mainloop()

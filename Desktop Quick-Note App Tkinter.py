import tkinter as tk
from tkinter import messagebox

def save_note():
    note_content = text_area.get("1.0", tk.END)
    with open("quick_note.txt", "w") as f:
        f.write(note_content)
    messagebox.showinfo("Success", "Note saved to quick_note.txt")

root = tk.Tk()
root.title("Python Quick-Note")
root.geometry("300x250")

text_area = tk.Text(root, height=10)
text_area.pack(pady=10)

save_btn = tk.Button(root, text="Save Note", command=save_note)
save_btn.pack()

root.mainloop()
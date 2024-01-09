import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename


def on_closing():
    """Fonction appelée lors de la fermeture de la fenêtre."""
    if messagebox.askokcancel("Quitter", "Le texte n'est pas sauvegardé. Voulez-vous enregistrer avant de quitter?"):
        save_file()
    else:
        window.destroy()


def open_file():
    """Ouvre un fichier pour éditer."""
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    """Sauvegarde le fichier actuel."""
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


def set_theme(theme):
    """Configure l'application selon le thème choisi."""
    if theme == "clair":
        colors = {"bg": "white", "fg": "black"}
    else:  # thème sombre
        colors = {"bg": "gray20", "fg": "white"}

    text_edit.config(bg=colors["bg"], fg=colors["fg"], insertbackground=colors["fg"])


# Création de la fenêtre principale
window = tk.Tk()
window.title("Bloc-notes")
window.geometry("700x600")
window.protocol("WM_DELETE_WINDOW", on_closing)

# Création de la barre de menu
menubar = tk.Menu(window)

# Menu Fichier
menu_file = tk.Menu(menubar, tearoff=0)
menu_file.add_command(label="New", command=lambda: text_edit.delete(1.0, tk.END))
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Quit", command=on_closing)
menubar.add_cascade(label="File", menu=menu_file)

# Menu Thème
menu_theme = tk.Menu(menubar, tearoff=0)
menu_theme.add_command(label="Clair", command=lambda: set_theme("clair"))
menu_theme.add_command(label="Sombre", command=lambda: set_theme("sombre"))
menubar.add_cascade(label="Thème", menu=menu_theme)

# Menu Aide
menu_help = tk.Menu(menubar, tearoff=0)
menu_help.add_command(label="About")
menubar.add_cascade(label="Help", menu=menu_help)

# Zone de texte pour écrire
text_edit = tk.Text(window)
text_edit.pack(expand=True, fill=tk.BOTH)

# Configuration initiale du thème
set_theme("clair")

# Configuration de la fenêtre pour afficher la barre de menu
window.config(menu=menubar)

# Lancement de la boucle principale

window.mainloop()

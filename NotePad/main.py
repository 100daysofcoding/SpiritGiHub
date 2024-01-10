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
    highlight_syntax()
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


def highlight_syntax(event=None):
    ''' Fonction pour mettre en évidence la syntaxe du Python dans l'éditeur de texte. '''
    # Désactivation de la mise en évidence pendant la mise à jour
    for tag in ["keyword", "string", "comment"]:
        text_edit.tag_remove(tag, "1.0", tk.END)

    # Expressions régulières pour différents éléments de syntaxe
    patterns = {
        "keyword": r"\b(import|as|from|def|return|class|if|elif|else|while|for|break|continue|try)\b",
        "string": r"\".*?\"|'.*?'",
        "comment": r"#.*"
    }

    # Mise en évidence de chaque élément
    for tag, pattern in patterns.items():
        start = "1.0"
        end = "end"
        while True:
            start = text_edit.search(pattern, start, stopindex=end, regexp=True)
            if not start:
                break
            stop = text_edit.index(f"{start}+{len(text_edit.get(start, f'{start} lineend'))}c")
            text_edit.tag_add(tag, start, stop)
            start = stop

    text_edit.tag_config("keyword", foreground="blue")
    text_edit.tag_config("string", foreground="green")
    text_edit.tag_config("comment", foreground="gray")


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

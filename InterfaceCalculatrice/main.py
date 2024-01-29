import tkinter as tk


def on_click(char):
    if char == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Erreur")
    elif char == 'C':
        entry.delete(0, tk.END)
    elif char == '+/-':
        try:
            current = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(-current))
        except Exception:
            pass
    else:
        entry.insert(tk.END, char)


root = tk.Tk()
root.title("Calculatrice")

entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('C', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('+', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+/-', 4, 2), ('*', 4, 3),
    ('%', 5, 0), ('=', 5, 1, 3), ('/', 5, 3)
]

for button_info in buttons:
    text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1
    button = tk.Button(root, text=text, width=10, height=2, command=lambda char=text: on_click(char))
    button.grid(row=row, column=col, columnspan=colspan, sticky='nsew')

root.mainloop()

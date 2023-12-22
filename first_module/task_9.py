import tkinter as tk

window = tk.Tk()
window.resizable(width=False, height=False)

entry = tk.Entry(fg='black', bg='white', width=25)



def print_label():
    text = entry.get()
    label = tk.Label(text=text)
    label.grid(row=2, column=1, padx=5, pady=5)

button = tk.Button(text='Вывести текст', command=print_label)

button.grid(row=1, column=1, padx=5, pady=5)
entry.grid(row=1, column=2, padx=5, pady=5)

window.mainloop()
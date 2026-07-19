import tkinter as tk
from tkinter import messagebox

tasks = []

##Funções
def add_task():
    task = entry_task.get().strip()

    if task:
        tasks.append(task)
        update_list()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa.")

def remove_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        update_list()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa.")

def update_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

#Janela
window = tk.Tk()
window.title("Lista de Tarefas")
window.geometry("400x400")

#Campo de entrada
entry_task = tk.Entry(window, width=35)
entry_task.pack(pady=10)

##Botão adicionar
btn_add = tk.Button(window, text="Adicionar", command=add_task)
btn_add.pack()

#Lista de tarefas
listbox = tk.Listbox(window, width=45, height=15)
listbox.pack(pady=10)

##Botão remover
btn_remove = tk.Button(window, text="Remover Selecionada", command=remove_task)
btn_remove.pack()

##Executar
window.mainloop()
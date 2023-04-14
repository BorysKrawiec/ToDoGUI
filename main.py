import tkinter as tk
from tkinter import LEFT, RIGHT, BOTH
from function import dodawanie, zaznacz, edytowanie, usuwanie, get_task_txt, save_task_txt

try:
    todo_list = get_task_txt()
except FileNotFoundError:
    print("Plik który próbujesz wczytać nie istnieje, program stworzy nowy, pusty plik")
    todo_list = []



padding = {"pady":5, "padx":5}

root = tk.Tk()
root.title("To Do App")
root.geometry("280x210")
root.resizable(False, False)

todo_list_var = tk.Variable(value=todo_list)
entry_var = tk.StringVar()

frm_todo = tk.Frame(root)
frm_todo.pack(**padding)

lbl_todo_text = tk.Label(frm_todo, text="Insert your to do ")
lbl_todo_text.pack(**padding)

ent_todo = tk.Entry(frm_todo, width=30, textvariable=entry_var)
ent_todo.pack(**padding)

frm_lower = tk.Frame(root)
frm_lower.pack(**padding)

frm_list = tk.Frame(frm_lower)
frm_list.pack(side=LEFT, **padding)

lst_todo = tk.Listbox(frm_list, height=5, listvariable=todo_list_var)
lst_todo.bind('<<ListboxSelect>>', lambda event, todo_list = todo_list, ent_todo = ent_todo, lst_todo = lst_todo: zaznacz(event, lst_todo, todo_list, ent_todo))
lst_todo.pack(side=LEFT, fill=BOTH, **padding)

scrollbar = tk.Scrollbar(frm_list)
lst_todo.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lst_todo.yview)
scrollbar.pack(side=RIGHT, fill=BOTH, **padding)

frm_buttons = tk.Frame(frm_lower)
frm_buttons.pack(side=LEFT, **padding)

btn_add = tk.Button(frm_buttons, text="Add", command=lambda entry_var = entry_var, todo_list = todo_list, lst_todo = lst_todo : dodawanie(entry_var, todo_list, lst_todo))
btn_add.pack(**padding)

btn_edit = tk.Button(frm_buttons, text="Edit", command=lambda lst_todo = lst_todo, todo_list = todo_list, ent_todo = ent_todo : edytowanie(lst_todo, todo_list, ent_todo))
btn_edit.pack(**padding)

btn_complete = tk.Button(frm_buttons, text="Complete", command=lambda lst_todo = lst_todo, todo_list = todo_list : usuwanie(lst_todo, todo_list))
btn_complete.pack(**padding)




root.mainloop()
import tkinter as tk
from tkinter import END


def dodawanie(entry_var, todo_list, lst_todo):
    todo_list.append(entry_var.get())
    lst_todo.insert(tk.END, entry_var.get())
    save_task_txt(todo_list)

def zaznacz(event, lst_todo, todo_list, ent_todo):
    if lst_todo.curselection():
        index_of_todo = lst_todo.curselection()[0]
        wybrany_todo = todo_list[index_of_todo]
        ent_todo.delete(0, END)
        ent_todo.insert(0, wybrany_todo)

def edytowanie(lst_todo, todo_list, ent_todo):
    index_of_todo = lst_todo.curselection()[0]
    new_value = ent_todo.get()
    todo_list[index_of_todo] = new_value
    lst_todo.delete(index_of_todo)
    lst_todo.insert(index_of_todo, new_value)
    save_task_txt(todo_list)

def usuwanie(lst_todo, todo_list):
    index_of_todo = lst_todo.curselection()[0]
    lst_todo.delete(index_of_todo)
    save_task_txt(todo_list)

def get_task_txt(file_path="to_do.txt"):
    with open(file_path, 'r')as file:
        return [line.replace('\n', '') for line in file.readlines()]


def save_task_txt(task_list, file_path="to_do.txt"):
    with open(file_path, 'w') as file:
        for task in task_list:
            file.write(task + "\n")
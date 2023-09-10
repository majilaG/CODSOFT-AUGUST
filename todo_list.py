import tkinter
import pickle
from tkinter import *
import tkinter.messagebox

rt=tkinter.Tk()
rt.title("My todo list")
def add_task():
   task=entry_task.get()
   if task != "":
     todo_task.insert(tkinter.END,task)
     entry_task.delete(0,tkinter.END)
   else:
     tkinter.messagebox.showwarning(title="warning",message="must enter a task")
def delete_task():
    try:
        task_index=todo_task.curselection()[0]
        todo_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="warning",message="select the task to delete")

def load_task():
    try:
        
       tasks=pickle.load(open("tasks.dat","rb"))
       todo_task.delete(0,tkinter.END) 

       for task in tasks:
          todo_task.insert(tkinter.END,task)
    except:
        tkinter.messagebox.showwarning(title="warning",message="create task to load it")
def save_task():
    tasks= todo_task.get(0,todo_task.size())
    pickle.dump(tasks,open("tasks.dat","wb"))    
fram_task=tkinter.Frame(rt)
fram_task.pack()
todo_task = tkinter.Listbox(fram_task, height=6, width=50)
todo_task.pack(side=tkinter.LEFT)
Scrollbar_task=tkinter.Scrollbar(fram_task)
Scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
todo_task.config(yscroll=Scrollbar_task.set)
Scrollbar_task.config(command=todo_task.yview)
entry_task= tkinter.Entry(rt,width=50)
entry_task.pack()
Button_add_task=tkinter.Button(rt,text="Add task",width=48,command=add_task)
Button_add_task.pack()
Button_delete_task=tkinter.Button(rt,text="delete task",width=48,command=delete_task)
Button_delete_task.pack()
Button_save_task=tkinter.Button(rt,text="save task",width=48,command=save_task)
Button_save_task.pack()
Button_load_task=tkinter.Button(rt,text="load task",width=48,command=load_task)
Button_load_task.pack()
rt.mainloop()

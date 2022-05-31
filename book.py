from tkinter import *
import tkinter as tk
import bookbackend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass


def view():
    list1.delete(0,END)  #To Empty List After Clicking Button Again And Again
    for rows in bookbackend.view_data():
        list1.insert(END,rows)

def search():
    list1.delete(0,END)
    for rows in bookbackend.search_data(title_value.get(),author_value.get(),year_value.get(),unq_value.get()):
        list1.insert(END,rows)

def insert():
    bookbackend.insert_data(title_value.get(),author_value.get(),year_value.get(),unq_value.get())
    list1.delete(0,END)
    list1.insert(END,(title_value.get(),author_value.get(),year_value.get(),unq_value.get()))

def update():
    bookbackend.update_data(selected_tuple[0],title_value.get(),author_value.get(),year_value.get(),unq_value.get())

def delete():
    bookbackend.delete_data(selected_tuple[0])

root=tk.Tk()
root.wm_title("Book_Inventory")
#labels
l1=Label(root,text="Title")
l1.grid(row=0,column=0)

l2=Label(root,text="Author")
l2.grid(row=0,column=2)

l3=Label(root,text="Year")
l3.grid(row=1,column=0)

l4=Label(root,text="Unique_ID")
l4.grid(row=1,column=2)

#Entry
title_value=StringVar()
e1=Entry(root,textvariable=title_value)
e1.grid(row=0,column=1)

author_value=StringVar()
e2=Entry(root,textvariable=author_value)
e2.grid(row=0,column=3)

year_value=StringVar()
e3=Entry(root,textvariable=year_value)
e3.grid(row=1,column=1)

unq_value=StringVar()
e4=Entry(root,textvariable=unq_value)
e4.grid(row=1,column=3)

#ListBox 
list1=Listbox(root,height=6,width=50)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#ScrollBar
scrb=Scrollbar(root)
scrb.grid(row=2,column=2,rowspan=7)


#Configuring ScrollBar With ListBOx
##yscrollcommand Used For Vertical Scrolling
list1.configure(yscrollcommand=scrb.set)
scrb.configure(command=list1.yview)

#Binding Scroll Bar
list1.bind('<<ListboxSelect>>',get_selected_row)


#Buttons
b1=Button(root,text="View All",width=15,command=view)
b1.grid(row=2,column=3)

b2=Button(root,text="Search Data",width=15,command=search)
b2.grid(row=3,column=3)

b3=Button(root,text="Add Data",width=15,command=insert)
b3.grid(row=4,column=3)

b4=Button(root,text="Update Data",width=15,command=update)
b4.grid(row=5,column=3)

b5=Button(root,text="Delete Data",width=15,command=delete)
b5.grid(row=6,column=3)

b6=Button(root,text="Close Application",width=15,command=root.destroy)
b6.grid(row=7,column=3)

root.mainloop()   


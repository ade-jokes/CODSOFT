from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from veiws import *

# Colors

co0 = '#F0FFFF'
co1 = '#000000'
co2 = '#4456f0'
co3 = '#ffffff'
co4 = '#0047AB'

window = tk.Tk()
window.title("")
window.geometry("575x450")
window.configure(background=co0)
window.resizable(width=False, height=False)

# Frames

frame_up = tk.Frame(window, width=600, height=50, bg=co2)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = tk.Frame(window, width=600, height=150, bg=co4)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = tk.Frame(window, width=600, height=300, bg=co0, relief='flat')
frame_table.grid(row=2, column=0, padx=10, pady=1)

# Functions

def show():
    global tree

    list_header = ['Name', 'Gender', 'Telephone', 'E-Mail']
    demo_list = view()
    
    tree = ttk.Treeview(frame_table, selectmode='extended', columns=list_header, show='headings')
    tree.pack(fill='both', expand=True)
    
    vsb = ttk.Scrollbar(frame_table, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient='horizontal', command=tree.xview)
    
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    

    # tree head
    tree.heading(0, text='Name', anchor='nw')
    tree.heading(1, text='Gender', anchor='nw')
    tree.heading(2, text='Telephone', anchor='nw')
    tree.heading(3, text='E-mail', anchor='nw')

    # Tree columns
    tree.column(0, width=120, anchor='nw')
    tree.column(1, width=100, anchor='nw')
    tree.column(2, width=100, anchor='nw')
    tree.column(3, width=180, anchor='nw')

    for item in demo_list:
        tree.insert('', 'end', values=item)

show()


def insert():
    name= e_name_1.get()
    gender=e_gender_1.get()
    telephone=e_telephone_1.get()
    email=e_email_1.get()
    
    data = [name, gender, telephone, email]
    
    if name== '' or gender=='' or email=='' or telephone=='':
        messagebox.showwarning('data','Please fill in all the feilds')
        
    else:
        add(data)
        messagebox.showinfo('data', 'data added sucessfully')
        e_name_1.delete(0,'end')
        e_gender_1.delete(0,'end')
        e_telephone_1.delete(0,'end')
        e_email_1.delete(0,'end')
        show()
        
def to_update():
    try:
        tree_data = tree. focus()
        tree_dictionary =tree.item(tree_data)
        tree_list = tree_dictionary['values']

        Name = str(tree_list[0])
        Gender = str(tree_list[1])
        Email= str(tree_list[2])
        Telephone= str(tree_list[3])
        
        e_name_1.insert(0, Name)
        e_gender_1.insert(0, Gender)
        e_email_1.insert(0, Email)
        e_telephone_1.insert(0, Telephone)
        
        def confirm():
            new_name = e_name_1.get()
            new_gender = e_gender_1.get()
            new_telephone = e_telephone_1.get()
            new_email = e_email_1.get()
            
            data = [new_name, new_gender, new_telephone, new_email]
            
            update(data)
            
            messagebox.showinfo('Success','data updated sucessfully')
            
            e_name_1.delete(0,'end')
            e_gender_1.delete(0,'end')
            e_telephone_1.delete(0,'end')
            e_email_1.delete(0,'end')
            
            for widget in frame_table.winfo_children():
                widget.destroy()
                
            b_confirm.destroy()
            
            show()
            
        b_confirm = tk.Button(frame_down, text="Confirm", width= 10, height= 1 , bg= co2, font= ('Ivy 8 bold'), command = confirm)
        b_confirm.place(x=290,y=110)
        
    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')
        
def to_remove():
    try:
        tree_data = tree. focus()
        tree_dictionary =tree.item(tree_data)
        tree_list = tree_dictionary['values']
        tree_telephone = str[tree_list]
        
        remove(tree_telephone)
        
        messagebox.showinfo('Sucess', 'Data has been deleted sucessfully')
        
        for widget in frame_table.winfo_children():
                widget.destroy()
                
        show()
        
    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')
        
        
def search():
    telephone = e_search.get()
    
    data = search(telephone)
    
    def delete_command():
        tree.delete(*tree.get_children())
        
    delete_command()
    
    for item in data:
        tree.insert('', 'end', values=item)
        

# Frame_up Widgets

app_name = tk.Label(frame_up, text='Phone-Book', height=1, font=('verdana 17 bold'), fg=co3, bg=co2)
app_name.place(x=5, y=5)

# frame_down widgets

name_1 = tk.Label(frame_down, text='Name ', width=20, height=1, font=('Ivy 10'), bg=co4, anchor='nw', fg=co3)
name_1.place(x=10, y=20)
e_name_1 = tk.Entry(frame_down, width=25, justify='left', highlightthickness=1, relief='solid')
e_name_1.place(x=80, y=20)

gender_1 = tk.Label(frame_down, text='Gender ', width=20, height=1, font=('Ivy 10'), bg=co4, anchor='nw', fg=co3)
gender_1.place(x=10, y=50)
e_gender_1 = ttk.Combobox(frame_down, width=25)
e_gender_1['values'] = ['', 'F', 'M']
e_gender_1.place(x=80, y=50)

telephone_1 = tk.Label(frame_down, text='Tel-no ', width=20, height=1, font=('Ivy 10'), bg=co4, anchor='nw', fg=co3)
telephone_1.place(x=10, y=80)
e_telephone_1 = tk.Entry(frame_down, width=25, justify='left', highlightthickness=1, relief='solid')
e_telephone_1.place(x=80, y=80)

email_1 = tk.Label(frame_down, text='Email ', width=20, height=1, font=('Ivy 10'), bg=co4, anchor='nw', fg=co3)
email_1.place(x=10, y=110)
e_email_1 = tk.Entry(frame_down, width=25, justify='left', highlightthickness=1, relief='solid')
e_email_1.place(x=80, y=110)

b_search = tk.Button(frame_down, text='Search', height=1, bg=co2, fg=co0, font=('Ivy 8 bold'), command= search)
b_search.place(x=330, y=20)
e_search = tk.Entry(frame_down, width=16, justify='left', font=('Ivy', 11), highlightthickness=1, relief='solid')
e_search.place(x=380, y=20)

b_view = tk.Button(frame_down, text='View', width=10, height=1, bg=co2, fg=co0, font=('Ivy 8 bold'), command= show)
b_view.place(x=340, y=50)

b_add = tk.Button(frame_down, text='Add', width=10, height=1, bg=co2, fg=co0, font=('Ivy 8 bold'), command= insert)
b_add.place(x=440, y=50)

b_update = tk.Button(frame_down, text='Update', width=10, height=1, bg=co2, fg=co0, font=('Ivy 8 bold'), command= to_update)
b_update.place(x=440, y=80)

b_delete = tk.Button(frame_down, text='Delete', width=10, height=1, bg=co2, fg=co0, font=('Ivy 8 bold'), command= to_remove)
b_delete.place(x=440, y=110)

window.mainloop()
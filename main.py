import tkinter
from tkinter import END,ANCHOR

#create main window
root=tkinter.Tk()
root.title("My TO Do List")
root.geometry("900x600")
root.title("My to do list")
root.resizable(0,0)

#variable
root_color="#F0E917"
title_font=("Segoe Script",22,"roman")
btn_color="#F8FF75"
btn_font=("Times New Roman",12)


#configure window
root.config(bg=root_color)


def malumot_qushish():
    qiymat = add_entry.get()
    list_box.insert(END,qiymat)
    add_entry.delete(0,END)

def tozalash():
    list_box.delete(0,END)  
    
def uchirish():
    list_box.delete(ANCHOR)

# def saqlash():
#     x = list_box.get(0,END)
#     with open('list.doc', 'w') as f:
#         for i in x:
#             if i.endswith("\n"):
#                 f.write(i)
#             else:
#                 f.write(i+"\n")
    
def saqlash():
    x = list_box.get(0,END)
    with open('./My_to_do_list/list.doc', 'w') as f:
        for i in x:
            if i.endswith("\n"):
                f.write(i)
            else:
                f.write(i+"\n")


def chiqish():
    root.quit()
            



#create title frame and its elements
frame_title=tkinter.Frame(root,bg=root_color)
lbl_title=tkinter.Label(frame_title,text="My to do list",bg=root_color,font=title_font)


#place on the window
lbl_title.grid(row=0,column=0)


#add items frame
frame_input=tkinter.Frame(root,bg=root_color)
#add entry and button widget
add_entry=tkinter.Entry(frame_input,width=25,font=btn_font)
add_btn=tkinter.Button(frame_input,text="Add to list",bg=btn_color,font=btn_font,command=malumot_qushish)

add_entry.grid(row=0,column=0,padx=5)
add_btn.grid(row=0,column=1,padx=5,ipadx=5)

frame_output=tkinter.Frame(root)
my_scrollbar=tkinter.Scrollbar(frame_output)
list_box=tkinter.Listbox(frame_output,width=45,height=8)

list_box.grid(row=0,column=0)
my_scrollbar.grid(row=0,column=1,sticky='NS')

list_box.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=list_box.yview)

frame_management=tkinter.Frame(root,bg=root_color)
btn_rem=tkinter.Button(frame_management,text="Delete",font=btn_font,bg=btn_color,command=uchirish)
btn_clear=tkinter.Button(frame_management,text="Cleaning",font=btn_font,bg=btn_color,command=tozalash)
btn_save=tkinter.Button(frame_management,text="Save to doc file",font=btn_font,bg=btn_color,command=saqlash)
btn_quit=tkinter.Button(frame_management,text="Exit",font=btn_font,bg=btn_color,command=chiqish)

btn_rem.grid(row=0,column=0,padx=5,ipadx=5)
btn_clear.grid(row=0,column=1,padx=5,ipadx=8)
btn_save.grid(row=0,column=2,padx=5,ipadx=10)
btn_quit.grid(row=0,column=3,padx=5,ipadx=10)



frame_title.pack(padx=10,pady=10)
frame_input.pack(padx=10,pady=10)
frame_output.pack(padx=10,pady=10)
frame_management.pack(padx=10,pady=10)


#mainloop
root.mainloop()








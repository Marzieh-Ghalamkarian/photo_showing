from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('photo')

frame_m=Frame(root,width=100,height=78)
frame_m.pack()

my_im = ImageTk.PhotoImage(Image.open('ja.jpg'))
my_im1 = ImageTk.PhotoImage(Image.open('download.jpg'))
my_im2 = ImageTk.PhotoImage(Image.open('kkk.jpg'))
lis=[my_im,my_im1,my_im2]

def ha(number_i):
    global mylable
    #global my_im
    #global my_im1
    #global my_im2
    for head in number_i:
       # global head
        mylable=Label(root,image=head)
        d=mylable.pack()
    #(my_im=Image.open('ja.jpg')
    #return my_im.show())
    ##my_im=ImageTk.PhotoImage(Image.open('ja.jpg'))
    #my_la1=Label(root,image=my_im)
    #my_la2=Label(root,image=my_im1)
    #my_la3=Label(root,image=my_im2)
    #my_la1.pack()
    #my_la2.pack()
    #my_la3.pack()

    return d    #my_la1,my_la2,my_la3

#entry=Entry(frame_m)
#entry.pack()

button_photo=Button(frame_m,text='show photo',command=lambda: ha(lis) )
button_photo.pack()

def exit_p():
    g=exit()
    return g

buttom_e=Button(root,text='exit',command=exit_p)
buttom_e.pack()

#**************************************************************
my_menu=Menu(root)
root.config(menu=my_menu)
#
file_m=Menu(my_menu)
my_menu.add_cascade(label='File',menu=file_m)
file_m.add_command(label='exit',command=exit_p)

def col():
    root.config(bg='red')
edit_m=Menu(my_menu)
my_menu.add_cascade(label='Edit',menu=edit_m)
edit_m.add_command(label='color',command=col)



root.mainloop()
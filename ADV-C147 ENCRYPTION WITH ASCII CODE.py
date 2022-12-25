from tkinter import *

root=Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background = 'snow')

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root, text = "Name in Ascii : ", bg="aqua")
label2 = Label(root, text = "Encrypted Name : ", bg="aqua")

def asciiConverter():
    input_word = enter_word.get()

    for letter in input_word :
        ascii = str(ord(letter))
        label["text"] += ascii + "  "
        
btn = Button(root,text="Show name in Ascii",command=asciiConverter, bg='gold', fg = 'black')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.6,anchor=CENTER)
label2.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()
from tkinter import *

class flappyUser:

    def __intit__(self):
        self.name = None
        self.avatar = None

    def getName(self):
        return self.name

    def getAvatar(self):
        return self.avatar
    
    def registerUser(self):
        root = Tk()
        root.geometry('500x300')
        root.title("Registration Form")

        fname = StringVar()
        avtr = StringVar()
        
        label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
        label_0.place(x=90,y=53)


        label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
        label_1.place(x=80,y=130)
        entry_1 = Entry(root,textvar=fname)
        entry_1.place(x=240,y=130)

        label_2 = Label(root, text="Avatar Name",width=20,font=("bold", 10))
        label_2.place(x=68,y=180)

        entry_2 = Entry(root,textvar=avtr)
        entry_2.place(x=240,y=180)

        Button(root, text='Submit',width=20,bg='brown',fg='white', command = root.destroy).place(x=180,y=230)
        root.mainloop()

        #root.close()

        self.name = fname.get()
        self.avatar = avtr.get()
       

from tkinter import *
from PIL import Image,ImageTk
class main: 
    #// make a class 
    def __init__(self,root):
        self.root=root

        self.root.title("MONTY HALL SIMULATION")
        self.root.geometry("800x500")
        self.root.maxsize(800,500)

        img1 = Image.open(r"image1.jpg")
        img1 = img1.resize((800, 500), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(img1)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)




        lbl_title = Label(self.root, text="MONTY HALL SIMULATION", font=("", 30), bg="#a2d2ff", fg="#023047",
                          bd=1)
        lbl_title.place(x=0, y=2, width=800, height=70)




        Hall_3_doors_prblm = Button(self.root,command=self.door_3,  text="3 Doors", font=("Roboto", 20), bg='#023047', fg="white")
        Hall_3_doors_prblm.place(x=180, y=230, height=60, width=150)
        Hall_4_doors_prblm = Button(self.root,command=self.door_4, text="4 Doors",font=("Roboto",20), bg='#023047', fg="white")
        Hall_4_doors_prblm.place(x=400, y=230, height=60, width=150)




        exit_gui = Button(self.root,  text="Exit",command=self.exit, font=("times new roman", 15),bg='red', fg="white")

        exit_gui.place(x=700, y=440, height=30, width=80)

    def door_3(self):
        self.root.destroy()
        from D3 import D3
        root = Tk()
        ob = D3(root)
        root.mainloop()

    def door_4(self):
        self.root.destroy()
        from D4 import D4
        root = Tk()
        ob = D4(root)
        root.mainloop()


    def exit(self):
        self.root.destroy()







if __name__ == '__main__':
    root = Tk()
    app = main(root)
    root.mainloop()

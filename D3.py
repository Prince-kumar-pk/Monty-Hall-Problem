from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from first import *
from tkinter import messagebox



class D3:
    def __init__(self,root):
        self.root=root
        # self.root.option_add( "*font", "CascadiaMono 14" )
        self.root.title("Monty Hall")
        self.root.geometry("1000x600+0+0")
        self.root.configure(bg="white")
        self.root.maxsize(1000, 600)
        #
        img1 = Image.open(r"3doors.jpg")
        img1 = img1.resize((1000, 600), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(img1)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # veriables
        self.var_test = StringVar()

        
        def ShowError1():
            messagebox.showerror("Input Error","Please give input !")
        def ShowError2():
            messagebox.showerror("Input Error","Please give valid input !")

        def show_graph():
            no_of_tests = self.test_no.get()
            if (no_of_tests == " "):
                ShowError1()
            elif (no_of_tests.isnumeric() == False):
                ShowError2()
                Clear_all()
            threedoor_graph(int(no_of_tests))

        def show_graph2():
            no_of_tests = self.test_no.get()
            if (no_of_tests == " "):
                ShowError1()
            elif (no_of_tests.isnumeric() == False):
                ShowError2()
                Clear_all()
            threedoor_graph2(int(no_of_tests))

        def Clear_all():
            txtfnumber1.delete(0,END)
            txtfnumber2.delete(0,END)
            txtfnumber3.delete(0,END)
            txtfnumber4.delete(0,END)

        def simulate():
            Clear_all()
            given_no_of_tests = self.test_no.get()
            if(given_no_of_tests == " "):
                ShowError1()
            elif (given_no_of_tests.isnumeric() == False and given_no_of_tests.isnumeric() == False):
                ShowError2()
                Clear_all()

            a= simulate_game(True,int(given_no_of_tests))
            b= simulate_game(False,int(given_no_of_tests))
            percentage_of_win_by_switch = round((a[0]/a[4])*100,2)
            percentage_of_loss_by_switch = round((a[2]/a[4])*100,2)
            percentage_of_win_without_switch = round((b[1]/b[4])*100,2)
            percentage_of_loss_without_switch = round((b[3]/b[4])*100,2)
            Clear_all()
            txtfnumber1.insert(0,percentage_of_win_by_switch)
            txtfnumber2.insert(0,percentage_of_loss_by_switch)
            txtfnumber3.insert(0,percentage_of_win_without_switch)
            txtfnumber4.insert(0,percentage_of_loss_without_switch)



        frame = Frame(self.root, bg="#a2d2ff").place(x=400, y=50, width=500, height=50)
        get_str = Label(frame, text=" MONTY HALL - THREE DOORS ", font=("Roboto", 20),  bg="#a2d2ff", fg="#023047")
        get_str.place(x=460, y=57)

        # -----------2nd frame----------

        frame1=Frame(self.root,bg="white").place(x=400,y=100,width=500,height=440)

        lbltest = Label(frame1, bg="white", font=("Roboto",16), text="Number of Simulation :", )
        lbltest.place(x=406, y=130)

        self.test_no = ttk.Entry(frame1, textvariable=self.var_test,font=("Roboto",16))
        self.test_no.place(x=630, y=130, width=160,height=30)

        Clear_btn = Button(frame, text="Clear All",command=Clear_all,font=("Roboto 10"),bg='aquamarine')
        Clear_btn.place(x=800, y=130, height=30, width=70)

        simulate_btn = Button(frame, text="Simulate",command=simulate,font=("Roboto 13"), bg='#caf0f8',fg="#000000")
        simulate_btn.place(x=600, y=170, height=40, width=120)

        graphshow1 = Button(frame, text="Show Graph 1", command=show_graph, font=("CascadiaMono 13"), bg='#caf0f8',
                            fg="#000000")
        graphshow1.place(x=600, y=250, height=40, width=120)

        graphshow2 = Button(frame, text="Show Graph 2", command=show_graph2, font=("CascadiaMono 13"), bg='#caf0f8',
                            fg="#000000")
        graphshow2.place(x=750, y=250, height=40, width=120)
      

        frame2 = LabelFrame(self.root,bg="white", bd=.5, relief=RIDGE, text="Result", font=("Roboto 15"),
                            padx=2)
        frame2.place(x=400, y=300, width=500, height=250)

        label_Using_switch1 = Label(frame2, font=("arial", 12, "bold"),bg="white", text="Win % using switch:", padx=2, pady=6)
        label_Using_switch1.grid(row=0, column=0, sticky=W)
        txtfnumber1 = ttk.Entry(frame2, font=("arial", 13, "bold"), width=27)
        txtfnumber1.grid(row=0, column=1)

        label_Using_switch2 = Label(frame2, font=("arial", 12, "bold"), bg="white", text="Lose % using switch:", padx=2, pady=6)
        label_Using_switch2.grid(row=1, column=0, sticky=W)
        txtfnumber2 = ttk.Entry(frame2, font=("arial", 13, "bold"), width=27)
        txtfnumber2.grid(row=1, column=1)

        label_without_switch1 = Label(frame2, font=("arial", 12, "bold"), bg="white", text="Win % without using switch:", padx=2, pady=6)
        label_without_switch1.grid(row=2, column=0, sticky=W)
        txtfnumber3 = ttk.Entry(frame2, font=("arial", 13, "bold"), width=27)
        txtfnumber3.grid(row=2, column=1)

        label_without_switch2 = Label(frame2, font=("arial", 12, "bold"), bg="white", text="Lose % without using switch:", padx=2, pady=6)
        label_without_switch2.grid(row=3, column=0, sticky=W)
        txtfnumber4 = ttk.Entry(frame2, font=("arial", 13, "bold"), width=27)
        txtfnumber4.grid(row=3, column=1)

        back_gui = Button(self.root, text="Back", command=self.back, font=("Roboto", 15), bg='gray', fg="white")

        back_gui.place(x=420, y=500, height=30, width=80)

        exit_gui = Button(self.root, text="Exit",command=self.exit, font=("Roboto", 15), bg='red', fg="white")

        exit_gui.place(x=800, y=500, height=30, width=80)

    #         -------------------Functions------------



    def reset_fields(self):
        self.test_no.delete(0,END)


    def exit(self):
        self.root.destroy()

    def back(self):
        self.root.destroy()

        from main import main
        root = Tk()
        app = main(root)
        root.mainloop()

if __name__ == '__main__':
    root=Tk()
    app=D3(root)
    root.mainloop()
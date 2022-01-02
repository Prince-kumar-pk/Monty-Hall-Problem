from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from first import *


class D4:
    def __init__(self, root):
        self.root = root
        self.root.title("Monty Hall")
        self.root.geometry("1000x600")
        self.root.configure(bg="white")
        self.root.maxsize(1000, 600)
        #********************************************************
        img1 = Image.open(r"d4.jpg")
        img1 = img1.resize((500, 600), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(img1)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=-300, y=0, relwidth=1, relheight=1)
  #***********************************************************************
        # veriables
        #
        self.var_test = StringVar()

        def ShowError1():
            messagebox.showerror("Input Error","Please give input !")
        def ShowError2():
            messagebox.showerror("Input Error","Please give valid input !")

        def show_graph1():
            no_of_tests = self.test_no.get()
            if (no_of_tests == " "):
                ShowError1()
            elif (no_of_tests.isnumeric() == False):
                ShowError2()
                Clear_all()
            fourdoor_graph1(int(no_of_tests))

        def show_graph2():
            no_of_tests = self.test_no.get()
            if (no_of_tests == " "):
                ShowError1()
            elif (no_of_tests.isnumeric() == False):
                ShowError2()
                Clear_all()
            fourdoor_graph2(int(no_of_tests))

        def show_graph3():
            no_of_tests = self.test_no.get()
            if (no_of_tests == " "):
                ShowError1()
            elif (no_of_tests.isnumeric() == False):
                ShowError2()
                Clear_all()
            fourdoor_graph3(int(no_of_tests))

        def show_graph4():
            no_of_tests = self.test_no.get()
            if (no_of_tests == " "):
                ShowError1()
            elif (no_of_tests.isnumeric() == False):
                ShowError2()
                Clear_all()
            fourdoor_graph4(int(no_of_tests))
        def Clear_all():
            txtfnumber1.delete(0,END)
            txtfnumber2.delete(0,END)
            txtfnumber3.delete(0,END)
            txtfnumber4.delete(0,END)
            txtfnumber5.delete(0,END)
            txtfnumber6.delete(0,END)
            txtfnumber7.delete(0,END)
            txtfnumber8.delete(0,END)

        def simulate():
            Clear_all()
            given_no_of_tests = self.test_no.get()
            if(given_no_of_tests == " "):
                ShowError1()
            elif (given_no_of_tests.isnumeric() == False ):
                ShowError2()
                Clear_all()
            
            z = simulate_game2(True,True,int(given_no_of_tests))
            x = simulate_game2(True,False,int(given_no_of_tests))
            w = simulate_game2(False,True,int(given_no_of_tests))
            y = simulate_game2(False,False,int(given_no_of_tests))
            percentage_of_win_by_two_switch = round((z[0]/z[8])*100,2)
            percentage_of_loss_by_two_switch = round((z[4]/z[8])*100,2)
            percentage_of_win_with_first_switch = round((x[2]/x[8])*100,2)
            percentage_of_loss_with_first_switch = round((x[7]/x[8])*100,2)
            percentage_of_win_with_second_switch = round((w[3]/x[8])*100,2)
            percentage_of_loss_with_second_switch = round((w[6]/x[8])*100,2)
            percentage_of_win_without_any_switch = round((y[1]/y[8])*100,2)
            percentage_of_loss_without_any_switch = round((y[5]/y[8])*100,2)
            txtfnumber1.insert(0,percentage_of_win_by_two_switch)
            txtfnumber2.insert(0,percentage_of_loss_by_two_switch)
            txtfnumber3.insert(0,percentage_of_win_with_first_switch)
            txtfnumber4.insert(0,percentage_of_loss_with_first_switch)
            txtfnumber5.insert(0,percentage_of_win_with_second_switch)
            txtfnumber6.insert(0,percentage_of_loss_with_second_switch)
            txtfnumber7.insert(0,percentage_of_win_without_any_switch)
            txtfnumber8.insert(0,percentage_of_loss_without_any_switch)
           


        frame = Frame(self.root, bg="#a2d2ff").place(x=400, y=5, width=550, height=50)
        get_str = Label(frame, text=" MONTY HALL - FOUR DOORS",font=("Roboto", 20), bg="#a2d2ff", fg="#023047")
        get_str.place(x=490, y=9)

        # -----------2nd frame----------

        frame1 = Frame(self.root, bg="white").place(x=400, y=50, width=550, height=440)

        lbltest = Label(frame1, bg="white", font=("Roboto",16), text="Number of Simulation:", )
        lbltest.place(x=410, y=80)

        self.test_no = ttk.Entry(frame1, textvariable=self.var_test,font=("Roboto",16))
        self.test_no.place(x=640, y=80, width=160, height=25)

        Clear_btn = Button(frame, text="Clear", command=Clear_all, bg='aquamarine')
        Clear_btn.place(x=820, y=80, height=30, width=60)

        simulate_btn = Button(frame, text="SIMULATE",font=("Roboto", 11), command=simulate, bg='#caf0f8')
        simulate_btn.place(x=600, y=120,height=40, width=120)

        graph_btn1 = Button(frame, text="Show Graph 1",font=("Roboto", 11),command=show_graph1,bg='#caf0f8')
        graph_btn1.place(x=440, y=170, height=40, width=100)
        graph_btn2 = Button(frame, text="Show Graph 2",font=("Roboto", 11),command=show_graph2,bg='#caf0f8')
        graph_btn2.place(x=560, y=170, height=40, width=100)
        graph_btn3 = Button(frame, text="Show Graph 3",font=("Roboto", 11),command=show_graph3, bg='#caf0f8')
        graph_btn3.place(x=680, y=170, height=40, width=100)
        graph_btn4 = Button(frame, text="Show Graph 4",font=("Roboto", 11),command=show_graph4, bg='#caf0f8')
        graph_btn4.place(x=800, y=170, height=40, width=100)

        frame2 = LabelFrame(self.root, bg="white", bd=.5, relief=RIDGE, text="Result", font=("arial", 15),
                            padx=2)
        frame2.place(x=400, y=240, width=550, height=350)

        label_Using_switch1 = Label(frame2, font=("arial", 12, "bold"), bg="white", text="Win % using Two switch :", padx=2,
                                    pady=6)
        label_Using_switch1.grid(row=0, column=0, sticky=W)
        txtfnumber1 = ttk.Entry(frame2, font=("arial", 13, "bold"), width=27)
        txtfnumber1.grid(row=0, column=1)

        label_Using_switch2 = Label(frame2, font=("arial", 12, "bold"), bg="white", text="Loose % using Two switch:",
                                    padx=2, pady=6)
        label_Using_switch2.grid(row=1, column=0, sticky=W)
        txtfnumber2 = ttk.Entry(frame2, font=("arial", 13, "bold"), width=27)
        txtfnumber2.grid(row=1, column=1)

        label_without_switch1 = Label(frame2, font=("arial", 12, "bold"), bg="white",
                                      text="Win % using First switch:", padx=2, pady=6)
        label_without_switch1.grid(row=2, column=0, sticky=W)
        txtfnumber3 = ttk.Entry(frame2, font=("arial", 13, "bold"), width=27)
        txtfnumber3.grid(row=2, column=1)

        label_without_switch2 = Label(frame2, font=("arial", 12, "bold"), bg="white",
                                      text="Loose % using First switch:", padx=2, pady=6)
        label_without_switch2.grid(row=3, column=0, sticky=W)
        txtfnumber4 = ttk.Entry(frame2, font=("arial", 13, "bold"), width=27)
        txtfnumber4.grid(row=3, column=1)

        ####

        label_without_switch2 = Label(frame2, font=("arial", 12, "bold"), bg="white",
                                      text="Win % using Second switch:", padx=2, pady=6)
        label_without_switch2.grid(row=4, column=0, sticky=W)
        txtfnumber5 = ttk.Entry(frame2, font=("arial", 13, "bold"), width=27)
        txtfnumber5.grid(row=4, column=1)

        ####

        label_without_switch2 = Label(frame2, font=("arial", 12, "bold"), bg="white",
                                      text="Loose % using Second switch:", padx=2, pady=6)
        label_without_switch2.grid(row=5, column=0, sticky=W)
        txtfnumber6 = ttk.Entry(frame2, font=("arial", 13, "bold"), width=27)
        txtfnumber6.grid(row=5, column=1)

        ###

        label_without_switch2 = Label(frame2, font=("arial", 12, "bold"), bg="white",
                                      text="Win % without using any switch:", padx=2, pady=6)
        label_without_switch2.grid(row=6, column=0, sticky=W)
        txtfnumber7 = ttk.Entry(frame2, font=("arial", 13, "bold"), width=27)
        txtfnumber7.grid(row=6, column=1)

        #

        label_without_switch2 = Label(frame2, font=("arial", 12, "bold"), bg="white",
                                      text="Loose % without using any switch:", padx=2, pady=6)
        label_without_switch2.grid(row=7, column=0, sticky=W)
        txtfnumber8 = ttk.Entry(frame2, font=("arial", 13, "bold"), width=27)
        txtfnumber8.grid(row=7, column=1)

        back_gui = Button(self.root, text="Back", command=self.back, font=("Roboto", 15), bg='gray', fg="white")

        back_gui.place(x=420, y=550, height=30, width=80)



        exit_gui = Button(self.root, text="Exit",command=self.exit, font=("Roboto Mono", 15), bg='red', fg="white")

        exit_gui.place(x=830, y=550, height=30, width=80)

    #         -------------------Functions------------

    def reset_fields(self):
        self.test_no.delete(0, END)

    def exit(self):
        self.root.destroy()

    def back(self):
        self.root.destroy()

        from main import main
        root = Tk()
        app = main(root)
        root.mainloop()


if __name__ == '__main__':
    root = Tk()
    app = D4(root)
    root.mainloop()
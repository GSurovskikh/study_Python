import  tkinter as tk

def start_demo():

    root= tk.Tk()
    lbl = tk.Label(root,text="button")
    lbl.grid(columnspan=3,row=0)

    frame1 = tk.Frame(root)
    btn1_frame1 = tk.Button(frame1,text="Кнопка")
    btn1_frame1.pack()
    btn2_frame1 = tk.Button(frame1, text="Кнопка")
    btn2_frame1.pack()
    btn3_frame1 = tk.Button(frame1, text="Кнопка")
    btn3_frame1.pack()
    frame1.grid(column=1,row=1)

    root.mainloop()

class ThreeButton(tk.Frame):
    def __init__(self,*args,**kwargs):
        super(ThreeButton,self).__init__(*args,**kwargs)
        self.btn1 = tk.Button(self,text="Btn")
        self.btn1.pack()
        self.btn2 = tk.Button(self, text="Btn")
        self.btn2.pack()
        self.btn3 = tk.Button(self, text="Btn")
        self.btn3.pack()


class DemoApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        super(DemoApp,self).__init__(*args,**kwargs)
        self.__lbl = tk.Label(self,text="Button")
        self.__lbl.grid(columnspan=3,row=0) #Был pack()
        self.frame1 = ThreeButton(self)
        self.frame1.grid(column=1,row=1)
        self.frame2 = ThreeButton(self)
        self.frame2.grid(column=2, row=1)
        self.frame3 = ThreeButton(self)
        self.frame3.grid(column=3, row=1)

        self.frame1.btn1.configure(command=lambda:self.change_label_text("Нажатие"))
        self.frame2.btn2.configure(command=lambda:self.change_label_text("Другое нажатие"))


    def change_label_text(self,new_text):
        self.__lbl.configure(text=new_text)

    def run(self):
        self.mainloop()



if __name__ == '__main__':
    #start_demo()

    app = DemoApp()
    app.run()

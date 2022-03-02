import tkinter as tk
class EasyCalcFrame(tk.Frame):
    def __init__(self,*args,**kwargs):
        super(EasyCalcFrame, self).__init__(*args,**kwargs)

        self.output = tk.Entry(self,state=tk.DISABLED)
        self.output.grid(columnspan=4,row=0)

        lbl_left_number = tk.Label(self,text="Первое число")
        lbl_left_number.grid(columnspan=2,row=1)

        lbl_right_number = tk.Label(self, text="Второе число")
        lbl_right_number.grid(column=2,columnspan=2,row=1)

        self.first_entry = tk.Entry(self)
        self.first_entry.grid(columnspan=2, row=2)

        self.second_entry = tk.Entry(self)
        self.second_entry.grid(column=2,columnspan=2, row=2)

        lbl_sum = tk.Button(self, text="+")
        lbl_sum.grid(row=3)

        lbl_minus = tk.Button(self, text="-")
        lbl_minus.grid(column=1, row=3)

        lbl_inc = tk.Button(self, text="*")
        lbl_inc.grid(column=2, row=3)

        lbl_div = tk.Button(self, text="/")
        lbl_div.grid(column=3, row=3)


class App(tk.Tk):
    def __init__(self,*args,**kwargs):
        super(App, self).__init__(*args,**kwargs)
        easy_calc_frame = EasyCalcFrame(self)
        easy_calc_frame.pack()
    def run(self):
        self.mainloop()
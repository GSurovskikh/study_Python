import tkinter as tk
from . import core


class EasyCalcFrame(tk.Frame):
    def __init__(self,*args,**kwargs):
        super(EasyCalcFrame, self).__init__(*args,**kwargs)

        self.output_text = tk.StringVar()
        self.output = tk.Entry(self,state=tk.DISABLED, textvariable=self.output_text)
        self.output.grid(columnspan=4,row=0)

        lbl_left_number = tk.Label(self,text="Первое число")
        lbl_left_number.grid(columnspan=2,row=1)

        lbl_right_number = tk.Label(self, text="Второе число")
        lbl_right_number.grid(column=2,columnspan=2,row=1)

        self.first_entry_text=tk.StringVar()
        self.first_entry = tk.Entry(self,textvariable=self.first_entry_text)
        self.first_entry.grid(columnspan=2, row=2)

        self.second_entry_text = tk.StringVar()
        self.second_entry = tk.Entry(self,textvariable=self.second_entry_text)
        self.second_entry.grid(column=2,columnspan=2, row=2)

        btn_add = tk.Button(self, text="+")
        btn_add.grid(row=3)

        btn_sub = tk.Button(self, text="-")
        btn_sub.grid(column=1, row=3)

        btn_mul = tk.Button(self, text="*")
        btn_mul.grid(column=2, row=3)

        btn_div = tk.Button(self, text="/")
        btn_div.grid(column=3, row=3)

        def action(left_value,right_value,op):
            result = op(left_value,right_value)
            self.output_text.set(result)
            self.first_entry_text.set("")
            self.second_entry_text.set("")

        btn_add.configure(
            command=lambda:action(
            self.first_entry_text.get(),
            self.second_entry_text.get(),
            core.do_addition
            )
        )
        btn_sub.configure(
            command=lambda: action(
                self.first_entry_text.get(),
                self.second_entry_text.get(),
                core.do_subtraction
            )
        )
        btn_mul.configure(
            command=lambda: action(
                self.first_entry_text.get(),
                self.second_entry_text.get(),
                core.do_mul
            )
        )
        btn_div.configure(
            command=lambda: action(
                self.first_entry_text.get(),
                self.second_entry_text.get(),
                core.do_div
            )
        )



class App(tk.Tk):
    def __init__(self,*args,**kwargs):
        super(App, self).__init__(*args,**kwargs)
        easy_calc_frame = EasyCalcFrame(self)
        easy_calc_frame.pack()
    def run(self):
        self.mainloop()
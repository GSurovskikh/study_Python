import functools
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

        button_data=[{"text": "+", "column": 0, "fn": core.do_addition},
                     {"text": "-", "column": 1, "fn": core.do_subtraction},
                     {"text": "*", "column": 2, "fn": core.do_mul},
                     {"text": "/", "column": 3, "fn": core.do_div}]

        def action(op):
            left_value = self.first_entry_text.get()
            right_value = self.second_entry_text.get()
            result = op(left_value,right_value)
            self.output_text.set(result)
            self.first_entry_text.set("")
            self.second_entry_text.set("")

        for record in button_data:
            btn = tk.Button(self,text=record["text"])
            btn.grid(column=record["column"],row=3)
            btn.configure(
                command=functools.partial(
                    action,
                    record["fn"]
                )
            )


class App(tk.Tk):
    def __init__(self,*args,**kwargs):
        super(App, self).__init__(*args,**kwargs)
        easy_calc_frame = EasyCalcFrame(self)
        easy_calc_frame.pack()
    def run(self):
        self.mainloop()
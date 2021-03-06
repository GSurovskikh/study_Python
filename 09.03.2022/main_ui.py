import tkinter as tk
import cloakroom as cr


class CloakroomUI(tk.Tk):
    def __init__(self,cloakroom_instance,*args,**kwargs):
        super(CloakroomUI, self).__init__(*args,**kwargs)

        if not isinstance(cloakroom_instance,cr.Cloakroom):
            raise TypeError("Не передан экземпляр класса Cloakroom")
        self.__cloakroom_instance = cloakroom_instance
        self.geometry("800x600+100+100")
        self.configure(padx=20,pady=20,bg="#ccc")


        btn_acquire_free_tag = tk.Button(self,text="Получить номерок",
                                         padx=10,pady=10,bg="#eef",
                                         command=self._acquire_free_tag)
        btn_acquire_free_tag.grid(column=0,row=0,rowspan=2)
        self._lbl_acqure_free_tag = tk.Label(self,bg="#fff")
        self._lbl_acqure_free_tag.grid(column=1,row=1)

        btn_return_tag = tk.Button(self, text="Вернуть номерок",
                                   padx=10, pady=10, bg="#eef",
                                   command=self._return_tag)
        btn_return_tag.grid(column=2, row=0, rowspan=2)
        self._lbl_return_tag = tk.Label(self, bg="#fff")
        self._lbl_return_tag.grid(column=3, row=1)

        self._ent_tag_string = tk.StringVar()
        ent_tag = tk.Entry(self,textvariable=self._ent_tag_string)
        ent_tag.grid(column=3,row=0)



    def _acquire_free_tag(self):
        try:
            tag = self.__cloakroom_instance.acquire_free_tag()
            self._lbl_acqure_free_tag.configure(text=f"Выдан номерок:{tag}")

        except cr.NotEnoughTagsError:
            self._lbl_acqure_free_tag.configure(text="Свободных номерков нет!")

    def _return_tag(self,tag):
        try:
            tag = self.__cloakroom_instance.return_tag(tag)
            self._lbl_return_tag.configure(text=f'Вернули номерок:{tag}')
        except cr.TagAlreadyReturnedError:
            self._lbl_return_tag.configure(text="Номерок уже в числе свободных")

    def run(self):
        self.mainloop()




if __name__ == '__main__':
    cloakroom = cr.Cloakroom(10)
    crui = CloakroomUI(cloakroom)
    crui.run()

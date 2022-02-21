class Human:
    def __init__(self,age="20",height="195",name="Аноним",gender="male"):
        self.age = int(age)
        self.height = float(height)
        self.name = name
        self.gender = gender


class Builder(Human):
    def __init__(self,**kwargs):
        super(Builder, self).__init__(**kwargs)
        self.preferable_tool = "None"

class Sailor(Human):
    def __init__(self, **kwargs):
        super(Sailor, self).__init__(**kwargs)
        self.preferable_tool = "None"


class Pilot(Human):
    def __init__(self,type_plane="Неопределено",flights_quantity="Неопределено",**kwargs):
        super(Pilot, self).__init__(**kwargs)
        self.type_plane = str(type_plane)
        self.flights_quantity = str(flights_quantity)

if __name__ == '__main__':

    h = Human(age=20,height=189,name="John",gender="male")

    print("--------")
    b = Builder()
    b.preferable_tool ="Шпатель"
    print("--------")
    s = Sailor()

    print("--------")
    p = Pilot(type_plane="fighter",flights_quantity=10)

    print(isinstance(b,Human))
    print(isinstance(s,Builder))
    print(issubclass(Pilot,Human))
class Human:
    def __init__(self,age,height,name,gender):
        self.age = int(age)
        self.height = float(height)
        self.name = name
        self.gender = gender


class Builder(Human):
    def __init__(self,age,height,name,gender,max_workweight,type_buildings):
        super(Builder, self).__init__(age,height,name,gender)
    

class Sailor(Human):
    def __init__(self,age,height,name,gender,type_cruise,voyages_quantity):
        super(Sailor, self).__init__(age,height,name,gender)


class Pilot(Human):
    def __init__(self,age,height,name,gender,type_plane,flights_quantity):
        super(Pilot, self).__init__(age,height,name,gender)



if __name__ == '__main__':

    h = Human(50,189,"John","male")

    print("--------")
    b = Builder(40,169,"Bob","male",10,"skyscraper")

    print("--------")
    s = Sailor(35, 165, "Kate", "female","ship",20)

    print("--------")
    p = Pilot(34, 175, "Bill", "male","fighter",100)

    print(isinstance(b,Human))
    print(isinstance(s,Builder))
    print(issubclass(Pilot,Human))
class Base:
    ...


class Derived(Base):
    ...


if __name__ == '__main__':
    var1 = Base()
    var2 = Derived()
    print(isinstance(var1,Base))
    print(isinstance(var2, Base))
    print(isinstance(var1, Derived))
    print(isinstance(var2, Derived))
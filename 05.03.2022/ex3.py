class Base:

    def do(self):
        return f"DO:{self.say()}"

    def say(self):
        return "---"


class A(Base):
    def __init__(self):
        super(A, self).__init__()

    def say(self):
        return "AAA"


class B(Base):
    def __init__(self):
        super(B, self).__init__()

    def say(self):
        return "BBB"

class C(Base):
    def __init__(self):
        super(C, self).__init__()

    def say(self):
        return "CCC"

if __name__ == '__main__':
    L = [A(),B(),C(),A(),B()]

    for elem in L:
        print(elem.say())

    print()

    for elem in L:
        print(elem.do())
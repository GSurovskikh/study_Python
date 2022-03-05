class A:

    def say(self):
        return "AAA"


class B:
    def say(self):
        return "BBB"

class C:
    def say(self):
        return "CCC"

if __name__ == '__main__':
    L = [A(),B(),C(),A(),B()]

    for elem in L:
        print(elem.say())
class Stack:
    pass  # Написать код стека здесь (можно использовать списки, ладно уж)


if __name__ == '__main__':

    # Создаём стек на 10 элементов
    s = Stack(10)  # Стек пуст!

    # Кладём в стек три объекта
    s.push("3434")
    s.push(3)
    s.push([1, 2, 4])

    # Вынимаем из стека объект и выводим его на экран
    obj = s.pop()  # После этой операции в стеке остаётся только 2 объекта!
    print(obj) # [1, 2, 4]
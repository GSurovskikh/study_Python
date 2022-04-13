class Deque:
    class EmptyError(Exception):
        def __init__(self, *args, message=None, **kwargs):
            if message is None:
                message = "Deque is empty."
            self.message = message
            super.__init__(self.message, *args)

    def __init__(self):
        self.__body = []

    def enqueue_tail(self,item):
        self.__body.append(item)

    def enqueue_head(self,item):
        self.__body.append(item)

    def dequeue_head(self):
        try:
            item = self.__body.pop(0)
        except IndexError:
            raise Deque.EmptyError

        return item

    def dequeue_tail(self):
        try:
            item = self.__body.pop()
        except IndexError:
            raise Deque.EmptyError

        return item

    def is_empty(self):
        return not self.__body

if __name__ == '__main__':

    d = Deque()
    d.enqueue_head("3454vcx")
    d.enqueue_head("4324")
    d.enqueue_head("432442342")
    d.enqueue_tail("fbbbb")

    while not d.is_empty():
        item = d.dequeue_head()
        print(item)
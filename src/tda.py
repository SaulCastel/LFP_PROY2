class node:
    def __init__(self,object) -> None:
        self.object = object
        self.next = None

    def get(self):
        return self.object

class sList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def __iter__(self):
        current = self.head
        while current != None:
            yield current.object
            current = current.next

    def __getitem__(self,index):
        if index == 0:
            return self.head
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            return curr

    def append(self, object):
        if self.size == 0:
            self.head = node(object)
        else:
            curr:node = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = node(object)
        self.size += 1
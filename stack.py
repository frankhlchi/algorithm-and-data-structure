
class Stack():
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def peek(self):
        if self.size() == 0:
            return
        return self.item[len(self.item)-1]

    def size(self):
        return len(self.item)

def test_stack():
    s = Stack()
    s.push(0)
    s.push(1)
    s.push(2)

    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0
    print ('test passed')


if __name__ == '__main__':
    test_stack()
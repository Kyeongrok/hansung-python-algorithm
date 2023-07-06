class Stack:
    arr = None
    top = 0

    def __init__(self, size=10000):
        self.arr = [None] * size

    def push(self, value):
        self.arr[self.top] = value
        self.top += 1

    def pop(self):
        if self.top == 0:
            raise Exception("Empty Stack")
        temp = self.arr[self.top - 1]
        self.top -= 1
        return temp

    def empty(self):
        return self.top == 0


st = Stack()
print(st.empty())
st.push(10)
st.pop()
print(st.empty())

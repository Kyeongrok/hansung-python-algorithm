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


st = Stack()
st.push(10)
st.pop()
st.pop()

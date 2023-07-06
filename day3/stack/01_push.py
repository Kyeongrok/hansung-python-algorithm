class Stack:
    arr = None
    top = 0

    def __init__(self, size = 10000):
        self.arr = [None] * size

    def push(self, value):
        self.arr[self.top] = value
        self.top += 1


st = Stack()
st.push(10)
st.push(20)
print(st.arr)
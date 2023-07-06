class Stack:
    arr = None
    top = 0

    def __init__(self, size = 10000):
        self.arr = [None] * size

    def push(self, value):
        self.arr[self.top] = value
        self.top += 1

    def pop(self):
        temp = self.arr[self.top - 1]
        self.top -= 1
        return temp

st = Stack()
st.push(10)
st.push(20)
print(st.arr)
val1 = st.pop()
print(val1, st.top)
print(st.arr)
val2 = st.pop()
print(val2, st.top)
print(st.arr)
st.push(30)
print(st.arr)

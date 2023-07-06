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

    def peek(self):
        if self.empty():
            raise Exception("Empty Stack")
        return self.arr[self.top - 1]


def is_valid_bracket(s):
    st = Stack()

    for c in s:
        if c == "(":
            print(c, "여는 괄호 일때는 push")
            st.push(c)
        else:
            print(c, "닫는 괄호 일때는 pop")
            st.pop()

    return st.empty()

s = '()((()))'
print(is_valid_bracket(s))

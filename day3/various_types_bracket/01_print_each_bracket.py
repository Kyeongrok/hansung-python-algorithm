from Stack import Stack


def is_valid_bracket(s):
    st = Stack()

    for c in s:
        if c == '(' or c == '{' or c == '[':
            print(c, '여는 괄호')
            st.push(c)
        else:
            print(c, '닫는 괄호')


print(is_valid_bracket('[{()}]'))

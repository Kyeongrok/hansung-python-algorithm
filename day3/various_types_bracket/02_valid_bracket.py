from Stack import Stack


def is_pair(first, second):
    if first == '(' and second == ')':
        return True
    elif first == '{' and second == '}':
        return True
    elif first == '[' and second == ']':
        return True
    return False


def is_valid_bracket(s):
    st = Stack(len(s))

    for c in s:
        if c == '(' or c == '{' or c == '[':
            st.push(c)
        else:
            if not st.empty() and is_pair(st.peek(), c):
                st.pop()
            else:
                return False

    return st.empty()

print(is_valid_bracket('[{()}]'))
print(is_valid_bracket('[{(}])'))
print(is_valid_bracket(']'))

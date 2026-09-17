def balanced(text):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in text:
        if ch in '([{':
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


print(balanced("([]{})"))
print(balanced("([)]"))
print(balanced("("))
print(balanced(""))
print(balanced("a(b)c[d]"))
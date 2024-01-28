stack = []
check = []
while True:
    s = input()
    if s == '.':
        break
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(')')

        elif s[i] == '[':
            stack.append(']')

        elif s[i] == ')':
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append('(')

        elif s[i] == ']':
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append('[')

    if not stack:
        check.append('o')
    else:
        check.append('x')
    stack = []

for j in check:
    if j == 'o':
        print('yes')
    elif j == 'x':
        print('no')
n = 0
stk = []
s = input()
for i in range(len(s)):
    if s[i] == '(':
        stk.append(')')
    elif stk and stk[-1] == ')':
        stk.pop()
        n += 2

print(len(s) - n)
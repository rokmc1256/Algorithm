import sys
input = sys.stdin.readline

stk =[]
result = 0
t = 1

s = input().strip()

for i in range(len(s)):
    if s[i] == '(':
        stk.append(s[i])
        t *= 2
    elif s[i] == '[':
        stk.append(s[i])
        t *= 3
    elif s[i] == ')':
        if not stk or stk[-1] == '[':
            result = 0
            break
        if s[i-1] == '(':
            result += t
        stk.pop()
        t //= 2
    else:
        if not stk or stk[-1] == '(':
            result = 0
            break
        if s[i-1] == '[':
            result += t
        stk.pop()
        t //= 3

if stk:
    print(0)
else:
    print(result)

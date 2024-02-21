import sys

input = sys.stdin.readline

stk = []
result = []

n = int(input())
for _ in range(n):
    s = input().split()

    if s[0] == 'push':
        stk.append(int(s[1]))
    elif s[0] == 'pop':
        if stk:
            result.append(stk.pop())
        else:
            result.append(-1)
    elif s[0] == 'size':
        result.append(len(stk))
    elif s[0] == 'empty':
        if stk:
            result.append(0)
        else:
            result.append(1)
    elif s[0] == 'top':
        if stk:
            result.append(stk[-1])
        else:
            result.append(-1)

for i in result:
    print(i)
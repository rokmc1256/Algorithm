import sys
input = sys.stdin.readline
stk = []
n = int(input())
for _ in range(n):
    result = 0
    t = 0
    s = input()
    for i in s:
        if i == 'O':
            t += 1
            result += t
        elif i == 'X':
            t = 0
            result += t
    stk.append(result)

for j in stk:
    print(j)
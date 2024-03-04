import sys
input = sys.stdin.readline

stk = []
s = list(input().strip())
target = list(input().strip())
n = len(target)
for i in s:
    stk.append(i)
    if stk[len(stk) - n : len(stk)] == target:
        for _ in range(n):
            stk.pop()

if stk:
    print(*stk, sep='')
else:
    print('FRULA')
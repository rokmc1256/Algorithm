import sys

input = sys.stdin.readline
n = 0
m, k = map(int, input().split())
stk = [[0] for _ in range(m)]

for _ in range(m):
    i, j = map(int, input().split())

    while stk[i][-1] > j:
        stk[i].pop()
        n += 1

    if stk[i][-1] == j:
        continue

    stk[i].append(j)
    n += 1

print(n)

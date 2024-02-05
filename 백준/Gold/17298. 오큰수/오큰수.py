import sys
input = sys.stdin.readline

stk = []
n = int(input())
arr = list(map(int, input().split()))
result = [-1] * n

for i in range(n - 1, -1, -1):
    while stk:
        if arr[i] < stk[-1]:
            result[i] = stk[-1]
            break
        else:
            stk.pop()
    stk.append(arr[i])
print(*result)
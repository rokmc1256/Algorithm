import sys
input = sys.stdin.readline
digit = {}
stk = []
n = int(input())
nums = list(map(int, input().split()))
result = [-1] * n

for i in nums:
    if i in digit:
        digit[i] += 1
    else:
        digit[i] = 1

for j in range(n - 1, -1, -1):
    while stk:
        if digit[nums[j]] < digit[stk[-1]]:
            result[j] = stk[-1]
            break
        else:
            stk.pop()
    stk.append(nums[j])

print(*result)
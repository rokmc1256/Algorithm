import sys
input = sys.stdin.readline
num = int(input())
result = [0] * num
stk = []
lazer_tops = list(map(int, input().split()))

for i in range(num):
    while stk:
        if stk[-1][1] > lazer_tops[i]:
            result[i] = stk[-1][0] + 1
            break
        else:
            stk.pop()
    stk.append([i, lazer_tops[i]])

print(*result)
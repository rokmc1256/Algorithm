import sys
input = sys.stdin.readline

result = 0
n = int(input())
nums = list(map(int, input().strip()))

for i in nums:
    result += i

print(result)
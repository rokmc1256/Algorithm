import sys
s = []
t = 1
input = sys.stdin.readline
n = int(input())
nums = wait = list(map(int, input().split()))

for i in range(len(nums)):
    if t == nums[i]:
        t += 1
        while s and s[-1] == t:
            s.pop()
            t += 1
    else:
        s.append(nums[i])

if not s:
    print('Nice')
    sys.exit()
else:
    for j in range(len(s)):
        if s[-1] == t:
            s.pop()
            t += 1
        else:
            print('Sad')
            sys.exit()

if not s:
    print('Nice')

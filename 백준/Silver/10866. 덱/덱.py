import sys
from collections import deque
input = sys.stdin.readline

deq = deque([])
result = []

n = int(input())

for _ in range(n):
    s = input().split()

    if s[0] == 'push_front':
        deq.appendleft(int(s[1]))
    elif s[0] == 'push_back':
        deq.append(int(s[1]))
    elif s[0] == 'pop_front':
        if deq:
            result.append(deq.popleft())
        else:
            result.append(-1)
    elif s[0] == 'pop_back':
        if deq:
            result.append(deq.pop())
        else:
            result.append(-1)
    elif s[0] == 'size':
        result.append(len(deq))
    elif s[0] == 'empty':
        if deq:
            result.append(0)
        else:
            result.append(1)
    elif s[0] == 'front':
        if deq:
            result.append(deq[0])
        else:
            result.append(-1)
    elif s[0] == 'back':
        if deq:
            result.append(deq[-1])
        else:
            result.append(-1)

for i in result:
    print(i)
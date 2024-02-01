import sys
input = sys.stdin.readline

stack = []
total = 0

n1 = int(input())
for _ in range(n1):
    n2 = int(input())
    stack.append(n2)

stick = stack[-1]

if stack:
    total += 1
    for j in range(len(stack) - 2, -1, -1):
        if stick < stack[j]:
            total += 1
            stick = stack[j]
print(total)
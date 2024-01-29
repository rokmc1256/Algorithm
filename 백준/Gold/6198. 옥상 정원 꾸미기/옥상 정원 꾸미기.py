stack1 = []
stack2 = []
n = int(input())
t = 0

for _ in range(n):
    s = int(input())
    stack1.append(s)

for i in stack1:
    while stack2 and stack2[-1] <= i:
        stack2.pop()

    stack2.append(i)
    t += len(stack2) - 1

print(t)
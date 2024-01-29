stack = []
n = 0
s = int(input())

for _ in range(s):
    AB_Word = input()
    for j in range(len(AB_Word)):
        if not stack:
            stack.append(AB_Word[j])
        else:
            if stack[-1] == AB_Word[j]:
                stack.pop()
            else:
                stack.append(AB_Word[j])

    if not stack:
        n += 1
    stack = []
print(n)
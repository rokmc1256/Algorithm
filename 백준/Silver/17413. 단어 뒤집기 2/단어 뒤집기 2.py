s = input()
stk = []
result = ''
check = False

for i in s:
    if i == '<':
        check = True
        for _ in range(len(stk)):
            result += stk.pop()

    stk.append(i)

    if i == '>':
        check = False
        for _ in range(len(stk)):
            result += stk.pop(0)

    if i == ' ' and check == False:
        for j in range(len(stk)):
            if j == 0:
                stk.pop()
                continue

            result += stk.pop()
        result += ' '

for _ in range(len(stk)):
    result += stk.pop()

print(result)
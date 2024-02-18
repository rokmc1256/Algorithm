result = []

while True:
    stk = []
    cnt = 0
    s = input()
    if '-' in s:
        break

    for i in s:
        if not stk and i == '}':
            cnt += 1
            stk.append('{')
        elif stk and i == '}':
            stk.pop()
        else:
            stk.append(i)

    cnt += len(stk) // 2
    result.append(cnt)

for j, k in enumerate(result, start = 1):
    print(f'{j}. {k}')
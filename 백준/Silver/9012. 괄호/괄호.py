t = []
result = []
n = int(input())
for _ in range(n):
    s = input()
    for j in range(len(s)):
        if s[j] == '(':
            t.append(s[j])
        elif t and t[-1] == '(' and s[j] == ')':
            t.pop()
        else:
            t.append(s[j])

    if not t:
        result.append('O')
    else:
        result.append('X')
    t = []

for k in result:
    if k == 'O':
        print('YES')
    elif k == 'X':
        print('NO')
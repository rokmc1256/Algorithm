import sys
stk = []
n = int(sys.stdin.readline())
for _ in range(n):
    s = sys.stdin.readline().split()

    if s[0] == '1':
        stk.append(s[1])

    elif s[0] == '2':
        if stk:
            print(stk.pop())
        else:
            print(-1)

    elif s[0] == '3':
        print(len(stk))

    elif s[0] == '4':
        if not stk:
            print(1)
        else:
            print(0)

    elif s[0] == '5':
        if stk:
            print(stk[-1])
        else:
            print(-1)


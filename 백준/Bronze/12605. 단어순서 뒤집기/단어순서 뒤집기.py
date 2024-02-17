stk = []
result = []
n = int(input())
for _ in range(n):
    s = input()
    d = s.split(' ')
    for _ in range(len(d)):
        stk.append(d.pop())

    result.append(' '.join(stk))
    stk = []


for i, j in enumerate(result, start = 1):
    print(f"Case #{i}: {j}")
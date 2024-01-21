def jaemin_jaehyun(num):
    stack = []
    sum  = 0
    for _ in range(num):
        nums = int(input())
        if nums == 0:
            if stack:
                stack.pop()
            else:
                continue
        else:
            stack.append(nums)

    if not stack:
        return 0
    else:
        for i in range(len(stack)):
            sum += stack[i]
    return sum

num = int(input())
print(jaemin_jaehyun(num))
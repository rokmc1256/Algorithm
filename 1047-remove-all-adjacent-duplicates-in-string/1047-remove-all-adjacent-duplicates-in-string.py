class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        stack.append(s[0])
        for num in range(len(s) - 1):
            if not stack:
                stack.append(s[num + 1])
            elif stack:
                if stack[-1] == s[num + 1]:
                    stack.pop()
                else:
                    stack.append(s[num + 1])

        return ''.join(stack)
        
class Solution(object):
    def makeGood(self, s):
        stack = []
        stack.append(s[0])
        for num in range(len(s) - 1):
            if not stack:
                stack.append(s[num + 1])
            elif stack:
                if stack[-1].lower() != s[num + 1].lower():
                    stack.append(s[num + 1])
                elif (stack[-1].islower() and s[num + 1].isupper()) or (stack[-1].isupper() and s[num + 1].islower()):
                    stack.pop()
                else:
                    stack.append(s[num + 1])

        return ''.join(stack)
        
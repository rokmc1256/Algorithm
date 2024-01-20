class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if s[i] != '*':
                stack.append(s[i])
            elif s[i] == '*':
                stack.pop()
            else:
                continue
        return ''.join(stack)
            
        
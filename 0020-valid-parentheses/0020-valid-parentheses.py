class Solution(object):
    def isValid(self, s):
        myArr = []
        dict = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        for data in s:
            if data in dict:
                myArr.append(data)
            elif len(myArr) == 0 or data != dict[myArr.pop()]:
                return False
        
        return len(myArr) == 0

        
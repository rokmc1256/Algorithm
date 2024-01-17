class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        sum_num = 0
        for data in operations:
            if data not in '+DC':
                stack.append(int(data))
            elif data == '+':
                stack.append(stack[-2] + stack[-1])
            elif data == 'D':
                stack.append(stack[-1] * 2)
            elif data == 'C':
                stack.pop()
        
        for num in stack:
            sum_num += num
        
        return sum_num
        
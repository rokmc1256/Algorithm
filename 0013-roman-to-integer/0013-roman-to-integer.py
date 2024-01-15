class Solution(object):
    def romanToInt(self, s):
        dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        total_num = 0
        data = 0

        while data < len(s) - 1:
            if dict[s[data]] < dict[s[data + 1]]:
                total_num += dict[s[data + 1]] - dict[s[data]]
                data += 2
            else:
                total_num += dict[s[data]]
                data += 1
        if data == len(s) - 1:
            total_num += dict[s[data]]
        return total_num
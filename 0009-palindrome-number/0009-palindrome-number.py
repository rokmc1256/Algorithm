class Solution(object):
    def isPalindrome(self, x):
        if x < 0 and x <= 1:
            return False   

        my_array1 = []

        while x > 0:
            num = x % 10
            my_array1.insert(0, num)
            x //= 10

        i = int(len(my_array1) / 2)

        n = 0
        while i > 0:
            if my_array1[n] != my_array1[int(len(my_array1)) - (n + 1)]:
                return False
            n += 1
            i -= 1
        return True
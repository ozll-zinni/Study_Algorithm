class Solution:
    def reverse(self, x: int) -> int:
        int_min, int_max = -2**31, 2**31-1

        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_num = 0

        while x != 0:
            digit = x % 10
            x //= 10
            
            if reversed_num > (int_max - digit) // 10:
                return 0 

            reversed_num = reversed_num * 10 + digit

        return sign * reversed_num
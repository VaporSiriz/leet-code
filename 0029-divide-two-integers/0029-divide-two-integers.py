class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        minus_flag = (dividend < 0) ^ (divisor < 0)
        quocient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            i = 0
            while dividend - (divisor << i) >= 0:
                # print(f"{dividend} - {(divisor << i)} >= {divisor}")
                i += 1
            value = divisor << (i if i==0 else (i-1))
            dividend -= value
            quocient += 1 << (i if i==0 else (i-1))
        if minus_flag:
            quocient = -quocient 
        if quocient >= 2147483648:
            quocient = 2147483647
        if quocient <= -2147483648:
            quocient = -2147483648
        return quocient
    
    # -2147483648 -1
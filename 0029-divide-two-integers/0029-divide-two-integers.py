class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        num = int(dividend/divisor)
        if num < -2147483648:
            return -2147483648

        if num > 2147483647:
            return 2147483647

        return num
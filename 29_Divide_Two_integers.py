class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max=2**31-1
        min=-2**31
        x = float (dividend/divisor)
        y=int(x)

        if y > max:
            return max
        if y < min:
            return min
            
        return y
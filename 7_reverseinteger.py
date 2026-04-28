class Solution:
    def reverse(self, x: int) -> int:
        n=x
        if x>0:
            rev_x=0
            maxva= 2**31-1
            minva=-2**31
            while x>0:
                digit=x%10
                rev_x= rev_x*10+digit
                x=x//10
        elif x < 0:
            x=-1*x
            rev_x=0
            maxva= 2**31-1
            minva =-2**31
            while x>0:
                digit=x%10
                rev_x= rev_x*10+digit
                x=x//10
        else:
            return 0

        if rev_x > maxva:
            return 0
        if rev_x < minva:
            return 0
        return(rev_x if n >= 0 else -rev_x)
        
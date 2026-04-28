class Solution:
    def addDigits(self, num: int) -> int:
        
        while num>=10:
            s= str(num)
            t=0
            for i in s:
                t+=int(i)
                num=t
        return num
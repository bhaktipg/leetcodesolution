class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        reverse_x = 0
        while x>0:
            digit = x%10
            reverse_x = reverse_x * 10 + digit
            x = x//10
        #print(reverse_x)

        if n == reverse_x:
            return True
        else:
            return False
        
    
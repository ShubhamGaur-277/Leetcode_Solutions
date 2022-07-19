class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        temp=x
        new=0
        temp2=0
        while(x!=0):
            new=new*10 + x%10
            x=int(x/10)
        
        return temp==new 
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        new=0
        temp2=0
        while(x!=0):
            temp2=x%10
            new=new*10 + temp2
            x=int(x/10)
        if(temp==new):
            return True 
        else: 
            return False
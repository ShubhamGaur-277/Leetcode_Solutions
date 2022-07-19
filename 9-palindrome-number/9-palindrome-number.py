class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x%10 ==0 and x!=0:
            return False
        temp=x
        new=0
        temp2=0
        while(x>new):
            new=new*10 + x%10
            x=int(x/10)
        return x == new or x == int(new/10)
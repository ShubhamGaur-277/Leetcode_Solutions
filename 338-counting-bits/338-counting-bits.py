class Solution:
    def countBits(self, n: int) -> List[int]:
        lst=[0]*(n+1)
        for i in range(1,n+1):
            if i%2!=0:
                lst[i]=1+lst[int(i/2)]
            else:
                lst[i]=lst[int(i/2)]
        return lst
            
        
class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n=len(code)
        ans=[]
        for i in range(n):
            total=0
            if k>0:
                for j in range(1,k+1):
                    total+=code[(i+j)%n]
            elif k<0:
                for j in range(1,abs(k)+1):
                    total+=code[(i-j)]
        
            ans.append(total)
        return ans
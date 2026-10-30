class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w=s.split()
        r=len(w[-1])
        return r
        

        
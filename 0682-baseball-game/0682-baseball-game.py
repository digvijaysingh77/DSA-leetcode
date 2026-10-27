class Solution:
    def calPoints(self, operations: list[str]) -> int:
        scores=[]
        for ch in operations:
            if ch=="C":
                scores.pop()
            elif ch=="D":
                scores.append(2*scores[-1])
            elif ch=="+":
                scores.append(scores[-1]+scores[-2])
            else:
                scores.append(int(ch))
        return sum(scores)
        
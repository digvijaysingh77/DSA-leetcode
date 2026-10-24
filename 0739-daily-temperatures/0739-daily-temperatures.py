class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = []
        stack = []

        for i in range(len(temperatures)):
            ans.append(0)

            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev

            stack.append(i)

        return ans
                    
                

        
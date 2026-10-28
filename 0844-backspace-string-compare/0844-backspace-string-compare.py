
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stack1 = []

        for ch in s:
            if ch == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)

        for cc in t:
            if cc == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(cc)

        return stack == stack1

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        myMap = {")" : "(", "]" : "[", "}" : "{"}
        for c in s:
            if c not in myMap:
                stack.append(c)
                continue
            if not stack or stack[-1] != myMap[c]:
                return False
            stack.pop()

        return not stack


        
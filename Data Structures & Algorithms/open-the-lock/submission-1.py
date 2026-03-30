class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        n = len(target)
        source = "0000"
        if source in deadends:
            return -1
        queue = deque([(source, 0)])
        vis = set()
        vis.add(source)
        while queue:
            s, c = queue.popleft()
            if s == target:
                return c

            if s in deadends:
                continue

            for i in range(len(s)):
                ch = s[i]
                op1 = s[:i] + str((int(ch) + 10 - 1)% 10) + s[i + 1:]
                op2 = s[:i] + str((int(ch) + 10 + 1)% 10) + s[i + 1:]
                if op1 not in vis:
                    vis.add(op1)
                    queue.append((op1, c + 1))
                if op2 not in vis:
                    vis.add(op2)
                    queue.append((op2, c + 1))

        return -1
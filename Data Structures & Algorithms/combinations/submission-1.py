class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(idx, curr):
            nonlocal ans
            if len(curr) == k:
                ans.append(curr.copy())
                return
            
            if idx == n + 1:
                return

            curr.append(idx)
            dfs(idx + 1, curr)
            curr.pop()
            dfs(idx + 1, curr)

        dfs(1, [])
        return ans


            

        
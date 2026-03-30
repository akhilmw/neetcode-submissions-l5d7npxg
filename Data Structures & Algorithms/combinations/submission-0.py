class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n + 1)]
        n = len(arr)
        ans = []


        def dfs(idx, curr):
            nonlocal ans
            if len(curr) == k:
                ans.append(curr.copy())
                return
            
            if idx == n:
                return

            curr.append(arr[idx])
            dfs(idx + 1, curr)
            curr.pop()
            dfs(idx + 1, curr)

        dfs(0, [])
        return ans


            

        
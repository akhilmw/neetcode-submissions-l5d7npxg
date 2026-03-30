class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        vis = [False] * n

        def dfs(node):
            vis[node] = True
            for it in adj[node]:
                if not vis[it]:
                    dfs(it)

        count = 0
        for i in range(n):
            if not vis[i]:
                count += 1
                dfs(i)

        return count
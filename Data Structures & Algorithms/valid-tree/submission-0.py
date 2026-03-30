class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [False] * n
        def dfs(node, parent):
            vis[node] = True
            for it in adj[node]:
                if not vis[it]:
                    if dfs(it, node):
                        return True
                elif it != parent:
                    return True

            return False

        
        for i in range(n):
            if not vis[i]:
                if dfs(i, -1):
                    return False

        return True


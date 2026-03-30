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

        
        has_cycle = dfs(0, -1)
        all_connected = True
        for val in vis:
            if val == False:
                all_connected = False
                break


        return not has_cycle and all_connected


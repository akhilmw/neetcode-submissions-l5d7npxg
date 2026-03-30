class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find_uPar(self, node):
        if self.parent[node] == node:
            return node

        self.parent[node] = self.find_uPar(self.parent[node])
        return self.parent[node]

    def union_by_size(self, node1, node2):
        u_par1 = self.find_uPar(node1)
        u_par2 = self.find_uPar(node2)

        if u_par1 == u_par2:
            return
        
        if self.size[u_par1] <= self.size[u_par2]: # smaller one goes and joins the bigger one
            self.parent[u_par1] = u_par2
            self.size[u_par2] += self.size[u_par1]
        elif self.size[u_par1] > self.size[u_par2]:
            self.parent[u_par2] = u_par1
            self.size[u_par1] += self.size[u_par2]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union_by_size(u, v)

        count = 0
        parent = dsu.parent
        for i in range(n):
            if i == parent[i]:
                count += 1

        return count

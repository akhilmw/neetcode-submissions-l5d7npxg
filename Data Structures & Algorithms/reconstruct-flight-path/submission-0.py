class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        destinations = defaultdict(list)
        for u, v in  tickets:
            destinations[u].append(v)

        for key in destinations.keys():
            destinations[key].sort()

        
        path = []

        def dfs(node):
            path.append(node)
            if len(path) == n + 1:
                return True

            for i in range(len(destinations[node])):
                dest = destinations[node][i]
                destinations[node].pop(i)
                if dfs(dest):
                    return True
                destinations[node].insert(i, dest)
            
            path.pop()
            return False

        dfs("JFK")
        return path
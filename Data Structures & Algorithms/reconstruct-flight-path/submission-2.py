class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        destinations = defaultdict(list)
        for u, v in  tickets:
            destinations[u].append(v)

        for key in destinations.keys():
            destinations[key].sort(reverse = True)

        
        path = []

        def dfs(node):

            while destinations[node]:
                dest = destinations[node].pop()
                dfs(dest)
            path.append(node)

        dfs("JFK")
        path.reverse()
        return path
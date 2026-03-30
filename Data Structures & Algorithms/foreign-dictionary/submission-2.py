class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adj = {}
        inDegree = {}
        
        
        for word in words:
            for char in word:
                if char not in adj:
                    adj[char] = set()
                    inDegree[char] = 0
        
        unique = len(adj)
        for i in range(n - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            x, y = 0, 0
            while x < len(word1) and y < len(word2) and word1[x] == word2[y]:
                x += 1
                y += 1
                
            if x < len(word1) and y < len(word2):
                if word2[y] not in adj[word1[x]]:
                    adj[word1[x]].add(word2[y])
                    inDegree[word2[y]] += 1
            elif x < len(word1): # breaks the lexi thing
                return ""
                
        ans = []
        queue = deque()
        
        for key, value in inDegree.items():
            if value == 0:
                queue.append(key)
        
        while queue:
            node = queue.popleft()
            ans.append(node)

            for it in adj[node]:
                inDegree[it] -= 1
                if inDegree[it] == 0:
                    queue.append(it)
        
        if len(ans) < unique:
            return ""
        
        return "".join(ans)
class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        pq = []
        counter = Counter(s)
        for k, v in counter.items():
            heapq.heappush(pq, (-v, k))
        
        ans = ""

        while pq:
            temp = []
            for _ in range(2):
                if pq:
                    temp.append(heapq.heappop(pq))
            
            if len(temp) == 1 and -temp[0][0] > 1:
                return ""
            
            st = ""
            for count, char in temp:
                st += char
                count = -count
                count -= 1
                if count > 0:
                    heapq.heappush(pq, (-count, char))
            ans += st

        return ans
        
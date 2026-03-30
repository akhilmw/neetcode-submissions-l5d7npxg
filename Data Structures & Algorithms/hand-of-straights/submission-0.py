class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        counter = Counter(hand)
        pq = []
        for k, v in counter.items():
            heapq.heappush(pq, (k, v))

        finalGroups = []
        while pq:
            group = []
            prev = None
            for _ in range(groupSize):
                if pq:
                    k, v = heapq.heappop(pq)
                    if not prev:
                        prev = k
                    elif k != prev + 1:
                        return False
                    else:
                        prev = k
                    group.append((k, v))


            if len(group) != groupSize:
                return False

            finalGroups.append(group)
            
            for k, v in group:
                v -= 1
                if v > 0:
                    heapq.heappush(pq, (k, v))
        
        return True
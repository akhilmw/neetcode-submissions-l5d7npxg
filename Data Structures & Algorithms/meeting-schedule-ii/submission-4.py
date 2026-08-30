"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda x : x.start)
        pq = [] # min heap
        rooms = 0

        for idx in range(n):
            while pq and pq[0] <= intervals[idx].start:
                heapq.heappop(pq)

            heapq.heappush(pq, (intervals[idx].end))
            rooms = max(rooms, len(pq))
        
        return rooms
        
                
        
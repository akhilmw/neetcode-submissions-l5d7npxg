"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key = lambda x : x.start)
        pq = []
        rooms = 0
 
        for i in range(len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            while pq and pq[0] <= start:
                heapq.heappop(pq)
            
            heapq.heappush(pq, end)
            rooms = max(rooms, len(pq))

        return rooms
            
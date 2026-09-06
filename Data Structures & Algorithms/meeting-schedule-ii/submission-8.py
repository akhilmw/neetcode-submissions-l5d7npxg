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

        mpp = defaultdict(int)

        for i in range(n):
            start, end = intervals[i].start, intervals[i].end
            mpp[start] += 1
            mpp[end] -= 1

        rooms = 0
        maxx = 0
        for key, value in sorted(mpp.items()):
            rooms += value
            maxx = max(maxx, rooms)

        return maxx
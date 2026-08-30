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

        for interval in intervals:
            mpp[interval.start] += 1
            mpp[interval.end] -= 1

        rooms = 0
        curr = 0
        for key in sorted(mpp.keys()):
            curr += mpp[key]
            rooms = max(rooms, curr)

        return rooms


        
                
        
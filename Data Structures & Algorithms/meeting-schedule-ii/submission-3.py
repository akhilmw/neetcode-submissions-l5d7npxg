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
        mpp = defaultdict(int)

        for interval in intervals:
            mpp[interval.start] += 1
            mpp[interval.end] -= 1
        
        curr = 0
        res = 0
        for _, value in sorted(mpp.items()):
            curr += value
            res = max(res, curr)

        return res
            
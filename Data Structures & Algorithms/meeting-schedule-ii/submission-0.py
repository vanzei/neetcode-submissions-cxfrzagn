"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        

        iS = 0
        iE = 0
        maxV = 0
        count = 0
        while iS < len(intervals):
            if start[iS] < end[iE]:
                count += 1
                iS += 1
            else:
                count -=1
                iE += 1
            maxV = max(count, maxV)

        return maxV


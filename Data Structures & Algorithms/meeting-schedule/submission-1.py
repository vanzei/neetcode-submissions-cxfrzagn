"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i : i.start)
        if not intervals or len(intervals) <=0:
            return True

        prevS, prevE = intervals[0].start, intervals[0].end
        for value in intervals[1:]:
            Cstart, Cend = value.start, value.end
            if Cstart < prevE:
                return False
            prevS, prevE = Cstart, Cend
        
        return True
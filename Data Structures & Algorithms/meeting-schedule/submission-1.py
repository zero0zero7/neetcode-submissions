"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        starts = [intervals[0].start]
        ends = [intervals[0].end]
        for inter in intervals[1:]:
            s = inter.start
            e = inter.end
            for i in range(len(starts)):
                started = starts[i]
                if s >= started:
                    if s < ends[i]:
                        return False
                    else:
                        continue
                else:
                    if e <= started:
                        break
                    else:
                        return False
            starts.append(s)
            ends.append(e)
        return True

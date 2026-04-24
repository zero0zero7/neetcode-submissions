"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        sorted_inters = sorted(intervals, key=lambda x: x.start)
        maxx = 1
        temp = 1
        # starts = [sorted_inters[0].start,]
        ends = [sorted_inters[0].end,]
        for inter in sorted_inters[1:]:
            next = False
            s = inter.start
            e = inter.end
            for idx in range(len(ends)):
                if s < ends[idx]:
                    # starts.append(s)
                    continue
                else:
                    ends[idx] = e
                    next = True
                    break
            if not next:
                ends.append(e)
        return len(ends)
            
        

        
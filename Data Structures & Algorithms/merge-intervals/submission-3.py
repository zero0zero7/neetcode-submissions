class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals_sorted = sorted(intervals, key=lambda x: x[0])
        prev_end = intervals_sorted[0][1]
        i = 1
        while i < len(intervals_sorted):
            start = intervals_sorted[i][0]
            if start <= prev_end:
                prev_end = max(prev_end, intervals_sorted[i][1])
                intervals_sorted.pop(i)
                if i == len(intervals_sorted):
                    intervals_sorted[i-1][1] = prev_end
                    return intervals_sorted
            else:
                intervals_sorted[i-1][1] = prev_end
                prev_end = max(prev_end, intervals_sorted[i][1])
                i += 1
        return intervals_sorted


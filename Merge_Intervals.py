

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        # write your code here
        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals, key=lambda v: v.start)
        start = intervals[0].start
        end = intervals[0].end
        i = 1
        while i < len(intervals):
            if end >= intervals[i].start:
                end = max(end, intervals[i].end)
                del intervals[i]
            else:
                intervals[i-1].start = start
                intervals[i-1].end = end
                start = intervals[i].start
                end = intervals[i].end
                i += 1
        intervals[i-1].start = start
        intervals[i-1].end = end
        
        return intervals


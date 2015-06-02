"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        
        if not intervals:
            return [newInterval]
        ret = []
        start = newInterval.start
        end = newInterval.end
        pos = 0
        for interval in intervals:
            if interval.end < start:
                ret.append(interval)
                pos += 1
            elif interval.start <= end:
                start = min(start, interval.start)
                end = max(end, interval.end)
            else:
                ret.append(interval)
        
        ret = ret[:pos] + [Interval(start, end)] + ret[pos:]
        return ret
            


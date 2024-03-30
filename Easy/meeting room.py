'''
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.
'''
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # we want sort the intervals based on the starting time to make it easier to compare
        intervals.sort(key = lambda i : i.start)
        # We want to compare the start time of next meeting with the end time of current
        for i in range(len(intervals)-1):
            if intervals[i+1].start < intervals[i].end:
                return False
        return True
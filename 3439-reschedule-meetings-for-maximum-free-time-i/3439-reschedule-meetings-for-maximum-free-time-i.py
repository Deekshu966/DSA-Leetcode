class Solution(object):
    def maxFreeTime(self,eventTime, k, startTime, endTime):
        n = len(startTime)
        gaps = []

        # First gap: before the first meeting
        gaps.append(startTime[0] - 0)

        # Gaps between meetings
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])

        # Last gap: after the last meeting
        gaps.append(eventTime - endTime[-1])

        # Sliding window of size k+1 over gaps array
        max_sum = curr_sum = sum(gaps[:k + 1])
        for i in range(k + 1, len(gaps)):
            curr_sum += gaps[i] - gaps[i - (k + 1)]
            max_sum = max(max_sum, curr_sum)

        return max_sum

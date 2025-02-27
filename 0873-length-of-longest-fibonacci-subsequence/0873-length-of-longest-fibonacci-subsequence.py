class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr_set = set(arr)
        max_len = 0
        for i in range(len(arr) - 1):
            for j in range(i+1,len(arr)):
                prev = arr[i]
                curr = arr[j]
                length = 2
                while prev + curr in arr_set:
                    length += 1
                    next = prev + curr
                    prev,curr = curr, next
                    max_len = max(max_len,length)
        return max_len
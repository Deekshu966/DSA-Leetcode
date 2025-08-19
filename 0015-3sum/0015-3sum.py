class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        nums.sort()     # sort once so triplets are consistent
        result = []     # directly store as lists
        n = len(nums)

        i = 0
        while i < n - 2:
            j = i + 1
            while j < n - 1:
                k = j + 1
                while k < n:
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        if triplet not in result:   # check duplicates manually
                            result.append(triplet)
                    k += 1
                j += 1
            i += 1

        return result
        """
        nums.sort()     # sort once so triplets are consistent
        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue   # skip duplicate for i

            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # skip duplicate j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # skip duplicate k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return result
class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        needed = nums[:]  # Copy of nums to track remaining values
        diff = [0] * (n + 1)  # Difference array for efficient range updates

        for k, (l, r, v) in enumerate(queries):
            # Apply range update using difference array
            diff[l] -= v
            if r + 1 < n:
                diff[r + 1] += v

            # Apply accumulated difference to the needed array
            current_decrement = 0
            all_zero = True  # Check if the array is fully zero

            for i in range(n):
                current_decrement += diff[i]
                needed[i] = max(0, needed[i] + current_decrement)  # Ensure non-negative
                if needed[i] > 0:
                    all_zero = False  # At least one element is non-zero

            if all_zero:
                return k + 1  # Return 1-based index

        return -1

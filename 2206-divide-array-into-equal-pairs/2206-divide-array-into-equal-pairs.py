class Solution(object):
    def divideArray(self, nums):
        nums.sort()  # Sort the array
        
        # Check if every two consecutive elements are equal
        for i in range(0, len(nums), 2):
            if nums[i] != nums[i + 1]:
                return False
        
        return True

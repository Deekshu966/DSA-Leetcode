class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            width = right - left
            curr_height = min(height[left], height[right])

            result = max(result, width * curr_height)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result
            
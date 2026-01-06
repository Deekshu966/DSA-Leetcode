"""
Example usage of array_utils.py with common LeetCode problems.
This file demonstrates how the utility functions can simplify solutions.
"""

from array_utils import ArrayUtils


class ExampleSolutions:
    """Example LeetCode solutions using array utilities."""
    
    # Problem 1: Two Sum
    # https://leetcode.com/problems/two-sum/
    @staticmethod
    def two_sum(nums, target):
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.
        
        Example:
            Input: nums = [2,7,11,15], target = 9
            Output: [0,1]
        """
        return ArrayUtils.two_sum_indices(nums, target)
    
    
    # Problem 26: Remove Duplicates from Sorted Array
    # https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    @staticmethod
    def remove_duplicates(nums):
        """
        Remove duplicates from sorted array in-place.
        Return the new length.
        
        Example:
            Input: nums = [1,1,2]
            Output: 2, nums = [1,2,_]
        """
        return ArrayUtils.remove_duplicates_sorted(nums)
    
    
    # Problem 27: Remove Element
    # https://leetcode.com/problems/remove-element/
    @staticmethod
    def remove_element(nums, val):
        """
        Remove all occurrences of val in-place.
        Return the new length.
        
        Example:
            Input: nums = [3,2,2,3], val = 3
            Output: 2, nums = [2,2,_,_]
        """
        return ArrayUtils.two_pointer_partition(nums, val)
    
    
    # Problem 53: Maximum Subarray
    # https://leetcode.com/problems/maximum-subarray/
    @staticmethod
    def max_subarray(nums):
        """
        Find the contiguous subarray with the largest sum.
        
        Example:
            Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
            Output: 6
            Explanation: [4,-1,2,1] has the largest sum = 6.
        """
        return ArrayUtils.kadane_max_subarray(nums)
    
    
    # Problem 189: Rotate Array
    # https://leetcode.com/problems/rotate-array/
    @staticmethod
    def rotate(nums, k):
        """
        Rotate the array to the right by k steps.
        
        Example:
            Input: nums = [1,2,3,4,5,6,7], k = 3
            Output: [5,6,7,1,2,3,4]
        """
        ArrayUtils.rotate_right(nums, k)
    
    
    # Problem 217: Contains Duplicate
    # https://leetcode.com/problems/contains-duplicate/
    @staticmethod
    def contains_duplicate(nums):
        """
        Return true if any value appears at least twice in the array.
        
        Example:
            Input: nums = [1,2,3,1]
            Output: true
        """
        return ArrayUtils.has_duplicates(nums)
    
    
    # Problem 283: Move Zeroes
    # https://leetcode.com/problems/move-zeroes/
    @staticmethod
    def move_zeroes(nums):
        """
        Move all 0's to the end while maintaining relative order.
        
        Example:
            Input: nums = [0,1,0,3,12]
            Output: [1,3,12,0,0]
        """
        ArrayUtils.move_zeros_to_end(nums)
    
    
    # Problem 350: Intersection of Two Arrays II
    # https://leetcode.com/problems/intersection-of-two-arrays-ii/
    @staticmethod
    def intersect(nums1, nums2):
        """
        Return an array of their intersection.
        Each element must appear as many times as it shows in both arrays.
        
        Example:
            Input: nums1 = [1,2,2,1], nums2 = [2,2]
            Output: [2,2]
        """
        nums1.sort()
        nums2.sort()
        return ArrayUtils.find_intersection_sorted(nums1, nums2)
    
    
    # Problem 704: Binary Search
    # https://leetcode.com/problems/binary-search/
    @staticmethod
    def search(nums, target):
        """
        Search for target in sorted array.
        Return its index, or -1 if not found.
        
        Example:
            Input: nums = [-1,0,3,5,9,12], target = 9
            Output: 4
        """
        return ArrayUtils.binary_search(nums, target)
    
    
    # Problem 1929: Concatenation of Array
    # https://leetcode.com/problems/concatenation-of-array/
    @staticmethod
    def get_concatenation(nums):
        """
        Return the concatenation of the array with itself.
        
        Example:
            Input: nums = [1,2,1]
            Output: [1,2,1,1,2,1]
        """
        return nums + nums
    
    
    # Problem 303: Range Sum Query - Immutable
    # https://leetcode.com/problems/range-sum-query-immutable/
    class NumArray:
        """
        Given an integer array nums, handle multiple queries
        to calculate the sum of elements between indices left and right.
        
        Example:
            Input: ["NumArray", "sumRange", "sumRange"]
                   [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5]]
            Output: [null, 1, -1]
        """
        
        def __init__(self, nums):
            self.prefix = ArrayUtils.prefix_sum(nums) if nums else []
        
        def sum_range(self, left, right):
            if not self.prefix:
                return 0
            if left == 0:
                return self.prefix[right]
            return self.prefix[right] - self.prefix[left - 1]


def demonstrate_usage():
    """Demonstrate how to use the utility functions."""
    
    print("=" * 60)
    print("Array Utilities - Example Usage")
    print("=" * 60)
    
    # Two Sum
    print("\n1. Two Sum")
    nums = [2, 7, 11, 15]
    target = 9
    result = ExampleSolutions.two_sum(nums, target)
    print(f"   Input: nums = {nums}, target = {target}")
    print(f"   Output: {result}")
    
    # Remove Duplicates
    print("\n2. Remove Duplicates from Sorted Array")
    nums = [1, 1, 2]
    length = ExampleSolutions.remove_duplicates(nums)
    print(f"   Input: nums = [1, 1, 2]")
    print(f"   Output: {length}, nums = {nums[:length]}")
    
    # Remove Element
    print("\n3. Remove Element")
    nums = [3, 2, 2, 3]
    val = 3
    length = ExampleSolutions.remove_element(nums, val)
    print(f"   Input: nums = [3, 2, 2, 3], val = {val}")
    print(f"   Output: {length}, nums = {nums[:length]}")
    
    # Maximum Subarray
    print("\n4. Maximum Subarray")
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = ExampleSolutions.max_subarray(nums)
    print(f"   Input: nums = {nums}")
    print(f"   Output: {result}")
    
    # Rotate Array
    print("\n5. Rotate Array")
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(f"   Input: nums = {nums}, k = {k}")
    ExampleSolutions.rotate(nums, k)
    print(f"   Output: {nums}")
    
    # Contains Duplicate
    print("\n6. Contains Duplicate")
    nums = [1, 2, 3, 1]
    result = ExampleSolutions.contains_duplicate(nums)
    print(f"   Input: nums = {nums}")
    print(f"   Output: {result}")
    
    # Move Zeroes
    print("\n7. Move Zeroes")
    nums = [0, 1, 0, 3, 12]
    print(f"   Input: nums = {nums}")
    ExampleSolutions.move_zeroes(nums)
    print(f"   Output: {nums}")
    
    # Intersection of Two Arrays
    print("\n8. Intersection of Two Arrays II")
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = ExampleSolutions.intersect(nums1.copy(), nums2.copy())
    print(f"   Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"   Output: {result}")
    
    # Binary Search
    print("\n9. Binary Search")
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = ExampleSolutions.search(nums, target)
    print(f"   Input: nums = {nums}, target = {target}")
    print(f"   Output: {result}")
    
    # Concatenation of Array
    print("\n10. Concatenation of Array")
    nums = [1, 2, 1]
    result = ExampleSolutions.get_concatenation(nums)
    print(f"   Input: nums = {nums}")
    print(f"   Output: {result}")
    
    # Range Sum Query
    print("\n11. Range Sum Query - Immutable")
    nums = [-2, 0, 3, -5, 2, -1]
    num_array = ExampleSolutions.NumArray(nums)
    print(f"   Input: nums = {nums}")
    print(f"   sumRange(0, 2) = {num_array.sum_range(0, 2)}")
    print(f"   sumRange(2, 5) = {num_array.sum_range(2, 5)}")
    print(f"   sumRange(0, 5) = {num_array.sum_range(0, 5)}")
    
    print("\n" + "=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    demonstrate_usage()

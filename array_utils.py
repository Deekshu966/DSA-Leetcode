"""
Array Utility Functions for LeetCode Problems

This module provides commonly used array manipulation functions
that can be reused across various LeetCode problems.
"""


class ArrayUtils:
    """Collection of utility functions for array operations."""
    
    @staticmethod
    def reverse(arr, start=None, end=None):
        """
        Reverse an array or a portion of it in-place.
        
        Args:
            arr: List to reverse
            start: Starting index (default: 0)
            end: Ending index (default: len(arr) - 1)
            
        Returns:
            None (modifies array in-place)
            
        Example:
            >>> arr = [1, 2, 3, 4, 5]
            >>> ArrayUtils.reverse(arr)
            >>> arr
            [5, 4, 3, 2, 1]
            
            >>> arr = [1, 2, 3, 4, 5]
            >>> ArrayUtils.reverse(arr, 1, 3)
            >>> arr
            [1, 4, 3, 2, 5]
        """
        if start is None:
            start = 0
        if end is None:
            end = len(arr) - 1
            
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    @staticmethod
    def rotate_right(arr, k):
        """
        Rotate array to the right by k positions in-place.
        
        Args:
            arr: List to rotate
            k: Number of positions to rotate
            
        Returns:
            None (modifies array in-place)
            
        Example:
            >>> arr = [1, 2, 3, 4, 5]
            >>> ArrayUtils.rotate_right(arr, 2)
            >>> arr
            [4, 5, 1, 2, 3]
        """
        if not arr:
            return
        
        n = len(arr)
        k = k % n
        
        if k == 0:
            return
        
        ArrayUtils.reverse(arr, 0, n - 1)
        ArrayUtils.reverse(arr, 0, k - 1)
        ArrayUtils.reverse(arr, k, n - 1)
    
    @staticmethod
    def rotate_left(arr, k):
        """
        Rotate array to the left by k positions in-place.
        
        Args:
            arr: List to rotate
            k: Number of positions to rotate
            
        Returns:
            None (modifies array in-place)
            
        Example:
            >>> arr = [1, 2, 3, 4, 5]
            >>> ArrayUtils.rotate_left(arr, 2)
            >>> arr
            [3, 4, 5, 1, 2]
        """
        if not arr:
            return
        
        n = len(arr)
        k = k % n
        
        if k == 0:
            return
        
        ArrayUtils.reverse(arr, 0, k - 1)
        ArrayUtils.reverse(arr, k, n - 1)
        ArrayUtils.reverse(arr, 0, n - 1)
    
    @staticmethod
    def binary_search(arr, target):
        """
        Perform binary search on a sorted array.
        
        Args:
            arr: Sorted list to search
            target: Element to find
            
        Returns:
            Index of target if found, -1 otherwise
            
        Example:
            >>> arr = [1, 2, 3, 4, 5, 6, 7]
            >>> ArrayUtils.binary_search(arr, 4)
            3
            >>> ArrayUtils.binary_search(arr, 8)
            -1
        """
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    @staticmethod
    def binary_search_leftmost(arr, target):
        """
        Find the leftmost occurrence of target in sorted array.
        
        Args:
            arr: Sorted list to search
            target: Element to find
            
        Returns:
            Index of leftmost occurrence, or -1 if not found
            
        Example:
            >>> arr = [1, 2, 2, 2, 3, 4, 5]
            >>> ArrayUtils.binary_search_leftmost(arr, 2)
            1
        """
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                result = mid
                right = mid - 1  # Continue searching left
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    @staticmethod
    def binary_search_rightmost(arr, target):
        """
        Find the rightmost occurrence of target in sorted array.
        
        Args:
            arr: Sorted list to search
            target: Element to find
            
        Returns:
            Index of rightmost occurrence, or -1 if not found
            
        Example:
            >>> arr = [1, 2, 2, 2, 3, 4, 5]
            >>> ArrayUtils.binary_search_rightmost(arr, 2)
            3
        """
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                result = mid
                left = mid + 1  # Continue searching right
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    @staticmethod
    def two_pointer_partition(arr, val):
        """
        Remove all occurrences of val in-place using two pointers.
        Returns new length.
        
        Args:
            arr: List to modify
            val: Value to remove
            
        Returns:
            New length after removing val
            
        Example:
            >>> arr = [3, 2, 2, 3, 4]
            >>> length = ArrayUtils.two_pointer_partition(arr, 3)
            >>> arr[:length]
            [2, 2, 4]
        """
        write = 0
        for read in range(len(arr)):
            if arr[read] != val:
                arr[write] = arr[read]
                write += 1
        return write
    
    @staticmethod
    def remove_duplicates_sorted(arr):
        """
        Remove duplicates from sorted array in-place.
        Returns new length.
        
        Args:
            arr: Sorted list to modify
            
        Returns:
            New length after removing duplicates
            
        Example:
            >>> arr = [1, 1, 2, 2, 3]
            >>> length = ArrayUtils.remove_duplicates_sorted(arr)
            >>> arr[:length]
            [1, 2, 3]
        """
        if not arr:
            return 0
        
        write = 0
        for read in range(1, len(arr)):
            if arr[read] != arr[write]:
                write += 1
                arr[write] = arr[read]
        return write + 1
    
    @staticmethod
    def has_duplicates(arr):
        """
        Check if array contains duplicates.
        
        Args:
            arr: List to check
            
        Returns:
            True if duplicates exist, False otherwise
            
        Example:
            >>> ArrayUtils.has_duplicates([1, 2, 3, 4])
            False
            >>> ArrayUtils.has_duplicates([1, 2, 2, 3])
            True
        """
        return len(arr) != len(set(arr))
    
    @staticmethod
    def is_sorted(arr, ascending=True):
        """
        Check if array is sorted.
        
        Args:
            arr: List to check
            ascending: True for ascending order, False for descending
            
        Returns:
            True if sorted, False otherwise
            
        Example:
            >>> ArrayUtils.is_sorted([1, 2, 3, 4])
            True
            >>> ArrayUtils.is_sorted([4, 3, 2, 1])
            False
            >>> ArrayUtils.is_sorted([4, 3, 2, 1], ascending=False)
            True
        """
        if len(arr) <= 1:
            return True
        
        if ascending:
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
        else:
            for i in range(1, len(arr)):
                if arr[i] > arr[i - 1]:
                    return False
        return True
    
    @staticmethod
    def prefix_sum(arr):
        """
        Calculate prefix sum array.
        
        Args:
            arr: Input list
            
        Returns:
            List where result[i] = sum(arr[0:i+1])
            
        Example:
            >>> ArrayUtils.prefix_sum([1, 2, 3, 4])
            [1, 3, 6, 10]
        """
        if not arr:
            return []
        
        result = [arr[0]]
        for i in range(1, len(arr)):
            result.append(result[-1] + arr[i])
        return result
    
    @staticmethod
    def prefix_product(arr):
        """
        Calculate prefix product array.
        
        Args:
            arr: Input list
            
        Returns:
            List where result[i] = product(arr[0:i+1])
            
        Example:
            >>> ArrayUtils.prefix_product([1, 2, 3, 4])
            [1, 2, 6, 24]
        """
        if not arr:
            return []
        
        result = [arr[0]]
        for i in range(1, len(arr)):
            result.append(result[-1] * arr[i])
        return result
    
    @staticmethod
    def move_zeros_to_end(arr):
        """
        Move all zeros to the end while maintaining relative order.
        
        Args:
            arr: List to modify
            
        Returns:
            None (modifies array in-place)
            
        Example:
            >>> arr = [0, 1, 0, 3, 12]
            >>> ArrayUtils.move_zeros_to_end(arr)
            >>> arr
            [1, 3, 12, 0, 0]
        """
        write = 0
        for read in range(len(arr)):
            if arr[read] != 0:
                arr[write] = arr[read]
                write += 1
        
        for i in range(write, len(arr)):
            arr[i] = 0
    
    @staticmethod
    def find_intersection_sorted(arr1, arr2):
        """
        Find intersection of two sorted arrays.
        
        Args:
            arr1: First sorted list
            arr2: Second sorted list
            
        Returns:
            List of common elements
            
        Example:
            >>> ArrayUtils.find_intersection_sorted([1, 2, 2, 3], [2, 2, 4])
            [2, 2]
        """
        result = []
        i, j = 0, 0
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                result.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
        
        return result
    
    @staticmethod
    def find_union_sorted(arr1, arr2):
        """
        Find union of two sorted arrays (without duplicates).
        
        Args:
            arr1: First sorted list
            arr2: Second sorted list
            
        Returns:
            Sorted list of unique elements from both arrays
            
        Example:
            >>> ArrayUtils.find_union_sorted([1, 2, 3], [2, 3, 4])
            [1, 2, 3, 4]
        """
        result = []
        i, j = 0, 0
        
        while i < len(arr1) and j < len(arr2):
            # Skip duplicates
            if result and arr1[i] == result[-1]:
                i += 1
                continue
            if result and arr2[j] == result[-1]:
                j += 1
                continue
            
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                result.append(arr2[j])
                j += 1
            else:
                result.append(arr1[i])
                i += 1
                j += 1
        
        # Add remaining elements
        while i < len(arr1):
            if not result or arr1[i] != result[-1]:
                result.append(arr1[i])
            i += 1
        
        while j < len(arr2):
            if not result or arr2[j] != result[-1]:
                result.append(arr2[j])
            j += 1
        
        return result
    
    @staticmethod
    def two_sum_indices(arr, target):
        """
        Find two indices whose values sum to target.
        
        Args:
            arr: Input list
            target: Target sum
            
        Returns:
            List of two indices, or empty list if not found
            
        Example:
            >>> ArrayUtils.two_sum_indices([2, 7, 11, 15], 9)
            [0, 1]
        """
        seen = {}
        for i, num in enumerate(arr):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
    
    @staticmethod
    def sliding_window_max(arr, k):
        """
        Find maximum element in each sliding window of size k.
        
        Args:
            arr: Input list
            k: Window size
            
        Returns:
            List of maximum values for each window
            
        Example:
            >>> ArrayUtils.sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3)
            [3, 3, 5, 5, 6, 7]
        """
        from collections import deque
        
        if not arr or k <= 0:
            return []
        
        result = []
        deq = deque()
        
        for i in range(len(arr)):
            # Remove elements outside window
            while deq and deq[0] < i - k + 1:
                deq.popleft()
            
            # Remove smaller elements from back
            while deq and arr[deq[-1]] < arr[i]:
                deq.pop()
            
            deq.append(i)
            
            # Add to result when window is full
            if i >= k - 1:
                result.append(arr[deq[0]])
        
        return result
    
    @staticmethod
    def kadane_max_subarray(arr):
        """
        Find maximum sum of contiguous subarray (Kadane's algorithm).
        
        Args:
            arr: Input list
            
        Returns:
            Maximum sum
            
        Example:
            >>> ArrayUtils.kadane_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
            6
        """
        if not arr:
            return 0
        
        max_sum = arr[0]
        current_sum = arr[0]
        
        for i in range(1, len(arr)):
            current_sum = max(arr[i], current_sum + arr[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum
    
    @staticmethod
    def flatten_2d_array(matrix):
        """
        Flatten a 2D array into a 1D array.
        
        Args:
            matrix: 2D list
            
        Returns:
            Flattened 1D list
            
        Example:
            >>> ArrayUtils.flatten_2d_array([[1, 2], [3, 4], [5, 6]])
            [1, 2, 3, 4, 5, 6]
        """
        result = []
        for row in matrix:
            result.extend(row)
        return result
    
    @staticmethod
    def transpose_matrix(matrix):
        """
        Transpose a 2D matrix.
        
        Args:
            matrix: 2D list
            
        Returns:
            Transposed matrix
            
        Example:
            >>> ArrayUtils.transpose_matrix([[1, 2, 3], [4, 5, 6]])
            [[1, 4], [2, 5], [3, 6]]
        """
        if not matrix or not matrix[0]:
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])
        result = [[matrix[r][c] for r in range(rows)] for c in range(cols)]
        return result


# Standalone utility functions for quick imports

def reverse_array(arr, start=None, end=None):
    """Convenience function for ArrayUtils.reverse"""
    return ArrayUtils.reverse(arr, start, end)


def rotate_array(arr, k, direction='right'):
    """
    Convenience function to rotate array.
    
    Args:
        arr: List to rotate
        k: Number of positions
        direction: 'right' or 'left'
    """
    if direction == 'right':
        ArrayUtils.rotate_right(arr, k)
    else:
        ArrayUtils.rotate_left(arr, k)


def binary_search(arr, target):
    """Convenience function for ArrayUtils.binary_search"""
    return ArrayUtils.binary_search(arr, target)


def two_sum(arr, target):
    """Convenience function for ArrayUtils.two_sum_indices"""
    return ArrayUtils.two_sum_indices(arr, target)

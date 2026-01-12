"""
Test suite for array utility functions.
Run with: python test_array_utils.py
"""

import sys
from array_utils import ArrayUtils


def test_reverse():
    """Test reverse function"""
    print("Testing reverse...")
    
    # Test full array reverse
    arr = [1, 2, 3, 4, 5]
    ArrayUtils.reverse(arr)
    assert arr == [5, 4, 3, 2, 1], f"Expected [5, 4, 3, 2, 1], got {arr}"
    
    # Test partial reverse
    arr = [1, 2, 3, 4, 5]
    ArrayUtils.reverse(arr, 1, 3)
    assert arr == [1, 4, 3, 2, 5], f"Expected [1, 4, 3, 2, 5], got {arr}"
    
    # Test empty array
    arr = []
    ArrayUtils.reverse(arr)
    assert arr == [], f"Expected [], got {arr}"
    
    # Test single element
    arr = [1]
    ArrayUtils.reverse(arr)
    assert arr == [1], f"Expected [1], got {arr}"
    
    print("✓ reverse tests passed")


def test_rotate():
    """Test rotate functions"""
    print("Testing rotate...")
    
    # Test rotate right
    arr = [1, 2, 3, 4, 5]
    ArrayUtils.rotate_right(arr, 2)
    assert arr == [4, 5, 1, 2, 3], f"Expected [4, 5, 1, 2, 3], got {arr}"
    
    # Test rotate right with k > len
    arr = [1, 2, 3]
    ArrayUtils.rotate_right(arr, 4)
    assert arr == [3, 1, 2], f"Expected [3, 1, 2], got {arr}"
    
    # Test rotate left
    arr = [1, 2, 3, 4, 5]
    ArrayUtils.rotate_left(arr, 2)
    assert arr == [3, 4, 5, 1, 2], f"Expected [3, 4, 5, 1, 2], got {arr}"
    
    # Test rotate with empty array
    arr = []
    ArrayUtils.rotate_right(arr, 2)
    assert arr == [], f"Expected [], got {arr}"
    
    print("✓ rotate tests passed")


def test_binary_search():
    """Test binary search functions"""
    print("Testing binary search...")
    
    # Test basic binary search
    arr = [1, 2, 3, 4, 5, 6, 7]
    assert ArrayUtils.binary_search(arr, 4) == 3, "Should find 4 at index 3"
    assert ArrayUtils.binary_search(arr, 8) == -1, "Should return -1 for missing element"
    assert ArrayUtils.binary_search(arr, 1) == 0, "Should find first element"
    assert ArrayUtils.binary_search(arr, 7) == 6, "Should find last element"
    
    # Test leftmost binary search
    arr = [1, 2, 2, 2, 3, 4, 5]
    assert ArrayUtils.binary_search_leftmost(arr, 2) == 1, "Should find leftmost 2"
    
    # Test rightmost binary search
    assert ArrayUtils.binary_search_rightmost(arr, 2) == 3, "Should find rightmost 2"
    
    # Test empty array
    assert ArrayUtils.binary_search([], 5) == -1, "Should return -1 for empty array"
    
    print("✓ binary search tests passed")


def test_two_pointer_partition():
    """Test two pointer partition"""
    print("Testing two pointer partition...")
    
    arr = [3, 2, 2, 3, 4]
    length = ArrayUtils.two_pointer_partition(arr, 3)
    assert arr[:length] == [2, 2, 4], f"Expected [2, 2, 4], got {arr[:length]}"
    
    arr = [1, 2, 3, 4, 5]
    length = ArrayUtils.two_pointer_partition(arr, 6)
    assert length == 5, "Should keep all elements when val not present"
    
    arr = [1, 1, 1]
    length = ArrayUtils.two_pointer_partition(arr, 1)
    assert length == 0, "Should remove all elements"
    
    print("✓ two pointer partition tests passed")


def test_remove_duplicates():
    """Test remove duplicates"""
    print("Testing remove duplicates...")
    
    arr = [1, 1, 2, 2, 3]
    length = ArrayUtils.remove_duplicates_sorted(arr)
    assert arr[:length] == [1, 2, 3], f"Expected [1, 2, 3], got {arr[:length]}"
    
    arr = [1, 1, 1, 1]
    length = ArrayUtils.remove_duplicates_sorted(arr)
    assert arr[:length] == [1], f"Expected [1], got {arr[:length]}"
    
    arr = []
    length = ArrayUtils.remove_duplicates_sorted(arr)
    assert length == 0, "Should return 0 for empty array"
    
    print("✓ remove duplicates tests passed")


def test_has_duplicates():
    """Test has duplicates"""
    print("Testing has duplicates...")
    
    assert ArrayUtils.has_duplicates([1, 2, 3, 4]) == False, "Should return False"
    assert ArrayUtils.has_duplicates([1, 2, 2, 3]) == True, "Should return True"
    assert ArrayUtils.has_duplicates([]) == False, "Empty array has no duplicates"
    assert ArrayUtils.has_duplicates([1]) == False, "Single element has no duplicates"
    
    print("✓ has duplicates tests passed")


def test_is_sorted():
    """Test is sorted"""
    print("Testing is sorted...")
    
    assert ArrayUtils.is_sorted([1, 2, 3, 4]) == True, "Should be sorted ascending"
    assert ArrayUtils.is_sorted([4, 3, 2, 1]) == False, "Should not be sorted ascending"
    assert ArrayUtils.is_sorted([4, 3, 2, 1], ascending=False) == True, "Should be sorted descending"
    assert ArrayUtils.is_sorted([1, 3, 2, 4]) == False, "Should not be sorted"
    assert ArrayUtils.is_sorted([]) == True, "Empty array is sorted"
    assert ArrayUtils.is_sorted([1]) == True, "Single element is sorted"
    
    print("✓ is sorted tests passed")


def test_prefix_operations():
    """Test prefix sum and product"""
    print("Testing prefix operations...")
    
    # Test prefix sum
    result = ArrayUtils.prefix_sum([1, 2, 3, 4])
    assert result == [1, 3, 6, 10], f"Expected [1, 3, 6, 10], got {result}"
    
    result = ArrayUtils.prefix_sum([])
    assert result == [], "Empty array should return empty"
    
    # Test prefix product
    result = ArrayUtils.prefix_product([1, 2, 3, 4])
    assert result == [1, 2, 6, 24], f"Expected [1, 2, 6, 24], got {result}"
    
    result = ArrayUtils.prefix_product([2, 3, 4])
    assert result == [2, 6, 24], f"Expected [2, 6, 24], got {result}"
    
    print("✓ prefix operations tests passed")


def test_move_zeros():
    """Test move zeros to end"""
    print("Testing move zeros...")
    
    arr = [0, 1, 0, 3, 12]
    ArrayUtils.move_zeros_to_end(arr)
    assert arr == [1, 3, 12, 0, 0], f"Expected [1, 3, 12, 0, 0], got {arr}"
    
    arr = [0, 0, 1]
    ArrayUtils.move_zeros_to_end(arr)
    assert arr == [1, 0, 0], f"Expected [1, 0, 0], got {arr}"
    
    arr = [1, 2, 3]
    ArrayUtils.move_zeros_to_end(arr)
    assert arr == [1, 2, 3], f"Expected [1, 2, 3], got {arr}"
    
    print("✓ move zeros tests passed")


def test_intersection_and_union():
    """Test intersection and union"""
    print("Testing intersection and union...")
    
    # Test intersection
    result = ArrayUtils.find_intersection_sorted([1, 2, 2, 3], [2, 2, 4])
    assert result == [2, 2], f"Expected [2, 2], got {result}"
    
    result = ArrayUtils.find_intersection_sorted([1, 2, 3], [4, 5, 6])
    assert result == [], f"Expected [], got {result}"
    
    # Test union
    result = ArrayUtils.find_union_sorted([1, 2, 3], [2, 3, 4])
    assert result == [1, 2, 3, 4], f"Expected [1, 2, 3, 4], got {result}"
    
    result = ArrayUtils.find_union_sorted([1, 1, 2], [2, 3, 3])
    assert result == [1, 2, 3], f"Expected [1, 2, 3], got {result}"
    
    print("✓ intersection and union tests passed")


def test_two_sum():
    """Test two sum"""
    print("Testing two sum...")
    
    result = ArrayUtils.two_sum_indices([2, 7, 11, 15], 9)
    assert result == [0, 1], f"Expected [0, 1], got {result}"
    
    result = ArrayUtils.two_sum_indices([3, 2, 4], 6)
    assert result == [1, 2], f"Expected [1, 2], got {result}"
    
    result = ArrayUtils.two_sum_indices([1, 2, 3], 10)
    assert result == [], f"Expected [], got {result}"
    
    print("✓ two sum tests passed")


def test_sliding_window_max():
    """Test sliding window maximum"""
    print("Testing sliding window max...")
    
    result = ArrayUtils.sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3)
    assert result == [3, 3, 5, 5, 6, 7], f"Expected [3, 3, 5, 5, 6, 7], got {result}"
    
    result = ArrayUtils.sliding_window_max([1], 1)
    assert result == [1], f"Expected [1], got {result}"
    
    result = ArrayUtils.sliding_window_max([1, -1], 1)
    assert result == [1, -1], f"Expected [1, -1], got {result}"
    
    print("✓ sliding window max tests passed")


def test_kadane():
    """Test Kadane's algorithm"""
    print("Testing Kadane's algorithm...")
    
    result = ArrayUtils.kadane_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert result == 6, f"Expected 6, got {result}"
    
    result = ArrayUtils.kadane_max_subarray([1])
    assert result == 1, f"Expected 1, got {result}"
    
    result = ArrayUtils.kadane_max_subarray([5, 4, -1, 7, 8])
    assert result == 23, f"Expected 23, got {result}"
    
    print("✓ Kadane's algorithm tests passed")


def test_matrix_operations():
    """Test matrix operations"""
    print("Testing matrix operations...")
    
    # Test flatten
    result = ArrayUtils.flatten_2d_array([[1, 2], [3, 4], [5, 6]])
    assert result == [1, 2, 3, 4, 5, 6], f"Expected [1, 2, 3, 4, 5, 6], got {result}"
    
    result = ArrayUtils.flatten_2d_array([[]])
    assert result == [], f"Expected [], got {result}"
    
    # Test transpose
    result = ArrayUtils.transpose_matrix([[1, 2, 3], [4, 5, 6]])
    expected = [[1, 4], [2, 5], [3, 6]]
    assert result == expected, f"Expected {expected}, got {result}"
    
    result = ArrayUtils.transpose_matrix([[1]])
    assert result == [[1]], f"Expected [[1]], got {result}"
    
    print("✓ matrix operations tests passed")


def run_all_tests():
    """Run all test functions"""
    print("=" * 50)
    print("Running Array Utils Test Suite")
    print("=" * 50)
    
    tests = [
        test_reverse,
        test_rotate,
        test_binary_search,
        test_two_pointer_partition,
        test_remove_duplicates,
        test_has_duplicates,
        test_is_sorted,
        test_prefix_operations,
        test_move_zeros,
        test_intersection_and_union,
        test_two_sum,
        test_sliding_window_max,
        test_kadane,
        test_matrix_operations,
    ]
    
    failed_tests = []
    
    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"✗ {test.__name__} FAILED: {e}")
            failed_tests.append(test.__name__)
        except Exception as e:
            print(f"✗ {test.__name__} ERROR: {e}")
            failed_tests.append(test.__name__)
    
    print("=" * 50)
    if failed_tests:
        print(f"FAILED: {len(failed_tests)} test(s) failed:")
        for test_name in failed_tests:
            print(f"  - {test_name}")
        sys.exit(1)
    else:
        print("SUCCESS: All tests passed! ✓")
        print("=" * 50)


if __name__ == "__main__":
    run_all_tests()

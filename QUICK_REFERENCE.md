# Array Utils Quick Reference

A quick reference guide for the most commonly used array utility functions.

## Import

```python
from array_utils import ArrayUtils
```

## Most Common Functions

### 🔄 Array Manipulation

```python
# Reverse
ArrayUtils.reverse(arr)                    # Reverse entire array
ArrayUtils.reverse(arr, start, end)        # Reverse portion

# Rotate
ArrayUtils.rotate_right(arr, k)            # [1,2,3,4,5] → [4,5,1,2,3] (k=2)
ArrayUtils.rotate_left(arr, k)             # [1,2,3,4,5] → [3,4,5,1,2] (k=2)

# Move zeros
ArrayUtils.move_zeros_to_end(arr)          # [0,1,0,3] → [1,3,0,0]
```

### 🔍 Searching

```python
# Binary search
ArrayUtils.binary_search(arr, target)              # Standard search
ArrayUtils.binary_search_leftmost(arr, target)     # Find first occurrence
ArrayUtils.binary_search_rightmost(arr, target)    # Find last occurrence

# Two sum
ArrayUtils.two_sum_indices(arr, target)            # Returns [i, j]
```

### ✂️ Two-Pointer Operations

```python
# Remove elements
ArrayUtils.two_pointer_partition(arr, val)         # Remove all val
ArrayUtils.remove_duplicates_sorted(arr)           # Remove duplicates

# Intersection & Union
ArrayUtils.find_intersection_sorted(arr1, arr2)    # Common elements
ArrayUtils.find_union_sorted(arr1, arr2)           # All unique elements
```

### 📊 Transformations

```python
# Prefix operations
ArrayUtils.prefix_sum(arr)                 # [1,2,3,4] → [1,3,6,10]
ArrayUtils.prefix_product(arr)             # [1,2,3,4] → [1,2,6,24]
```

### ✅ Validation

```python
# Check array properties
ArrayUtils.has_duplicates(arr)             # True/False
ArrayUtils.is_sorted(arr)                  # True/False (ascending)
ArrayUtils.is_sorted(arr, ascending=False) # True/False (descending)
```

### 🎯 Advanced Algorithms

```python
# Sliding window maximum
ArrayUtils.sliding_window_max(arr, k)      # Max in each window of size k

# Maximum subarray (Kadane's)
ArrayUtils.kadane_max_subarray(arr)        # Max sum of contiguous subarray
```

### 📐 Matrix Operations

```python
# Matrix operations
ArrayUtils.flatten_2d_array(matrix)        # 2D → 1D
ArrayUtils.transpose_matrix(matrix)        # Transpose rows/cols
```

## LeetCode Problem Patterns

| Problem Type | Use This Function |
|-------------|-------------------|
| Two Sum | `two_sum_indices()` |
| Remove Duplicates | `remove_duplicates_sorted()` |
| Remove Element | `two_pointer_partition()` |
| Rotate Array | `rotate_right()` or `rotate_left()` |
| Move Zeroes | `move_zeros_to_end()` |
| Binary Search | `binary_search()` |
| Maximum Subarray | `kadane_max_subarray()` |
| Array Intersection | `find_intersection_sorted()` |
| Range Sum Query | `prefix_sum()` |
| Contains Duplicate | `has_duplicates()` |
| Check if Sorted | `is_sorted()` |

## Convenience Functions

```python
from array_utils import reverse_array, rotate_array, binary_search, two_sum

# Use without ArrayUtils prefix
reverse_array(arr)
rotate_array(arr, 2, direction='right')
binary_search(arr, target)
two_sum(arr, target)
```

## Time Complexity Reference

| Function | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| reverse | O(n) | O(1) |
| rotate | O(n) | O(1) |
| binary_search | O(log n) | O(1) |
| two_sum | O(n) | O(n) |
| remove_duplicates | O(n) | O(1) |
| move_zeros | O(n) | O(1) |
| prefix_sum | O(n) | O(n) |
| intersection | O(m + n) | O(min(m,n)) |
| sliding_window_max | O(n) | O(k) |
| kadane | O(n) | O(1) |

## Tips

1. **In-place functions** return `None` - they modify the array directly
2. **Convenience functions** return the modified array for chaining
3. **Sorted arrays** - intersection/union functions expect sorted inputs
4. **Binary search** - requires sorted array
5. **Edge cases** - all functions handle empty arrays and single elements

## Running Tests

```bash
python test_array_utils.py
```

## Examples

```bash
python array_utils_examples.py
```

## Documentation

See `ARRAY_UTILS_README.md` for complete documentation with detailed examples.

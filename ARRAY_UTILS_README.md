# Array Utility Functions

A comprehensive collection of reusable array manipulation and algorithm utilities for solving LeetCode problems and general programming challenges.

## Overview

This module (`array_utils.py`) provides an `ArrayUtils` class with static methods for common array operations, including:
- Array manipulation (reverse, rotate, swap)
- Binary search variants
- Two-pointer techniques
- Prefix operations
- Sliding window algorithms
- Matrix operations
- And much more!

## Installation

Simply copy `array_utils.py` to your project directory and import it:

```python
from array_utils import ArrayUtils

# Or import specific convenience functions
from array_utils import reverse_array, rotate_array, binary_search, two_sum
```

## Usage Examples

### Basic Array Manipulation

#### Reverse Array
```python
arr = [1, 2, 3, 4, 5]
ArrayUtils.reverse(arr)
# arr is now [5, 4, 3, 2, 1]

# Reverse a portion
arr = [1, 2, 3, 4, 5]
ArrayUtils.reverse(arr, 1, 3)
# arr is now [1, 4, 3, 2, 5]
```

#### Rotate Array
```python
# Rotate right
arr = [1, 2, 3, 4, 5]
ArrayUtils.rotate_right(arr, 2)
# arr is now [4, 5, 1, 2, 3]

# Rotate left
arr = [1, 2, 3, 4, 5]
ArrayUtils.rotate_left(arr, 2)
# arr is now [3, 4, 5, 1, 2]
```

### Searching Algorithms

#### Binary Search
```python
arr = [1, 2, 3, 4, 5, 6, 7]

# Basic binary search
index = ArrayUtils.binary_search(arr, 4)
# Returns 3

# Find leftmost occurrence
arr = [1, 2, 2, 2, 3, 4, 5]
index = ArrayUtils.binary_search_leftmost(arr, 2)
# Returns 1

# Find rightmost occurrence
index = ArrayUtils.binary_search_rightmost(arr, 2)
# Returns 3
```

#### Two Sum
```python
arr = [2, 7, 11, 15]
indices = ArrayUtils.two_sum_indices(arr, 9)
# Returns [0, 1]
```

### Two-Pointer Techniques

#### Remove Elements
```python
arr = [3, 2, 2, 3, 4]
length = ArrayUtils.two_pointer_partition(arr, 3)
# arr[:length] is [2, 2, 4]
```

#### Remove Duplicates from Sorted Array
```python
arr = [1, 1, 2, 2, 3]
length = ArrayUtils.remove_duplicates_sorted(arr)
# arr[:length] is [1, 2, 3]
```

#### Move Zeros to End
```python
arr = [0, 1, 0, 3, 12]
ArrayUtils.move_zeros_to_end(arr)
# arr is now [1, 3, 12, 0, 0]
```

### Array Intersection and Union

```python
# Intersection
result = ArrayUtils.find_intersection_sorted([1, 2, 2, 3], [2, 2, 4])
# Returns [2, 2]

# Union
result = ArrayUtils.find_union_sorted([1, 2, 3], [2, 3, 4])
# Returns [1, 2, 3, 4]
```

### Prefix Operations

```python
# Prefix sum
arr = [1, 2, 3, 4]
result = ArrayUtils.prefix_sum(arr)
# Returns [1, 3, 6, 10]

# Prefix product
result = ArrayUtils.prefix_product(arr)
# Returns [1, 2, 6, 24]
```

### Sliding Window

```python
arr = [1, 3, -1, -3, 5, 3, 6, 7]
result = ArrayUtils.sliding_window_max(arr, 3)
# Returns [3, 3, 5, 5, 6, 7]
```

### Maximum Subarray (Kadane's Algorithm)

```python
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = ArrayUtils.kadane_max_subarray(arr)
# Returns 6 (subarray [4, -1, 2, 1])
```

### Matrix Operations

```python
# Flatten 2D array
matrix = [[1, 2], [3, 4], [5, 6]]
result = ArrayUtils.flatten_2d_array(matrix)
# Returns [1, 2, 3, 4, 5, 6]

# Transpose matrix
matrix = [[1, 2, 3], [4, 5, 6]]
result = ArrayUtils.transpose_matrix(matrix)
# Returns [[1, 4], [2, 5], [3, 6]]
```

### Validation Functions

```python
# Check for duplicates
has_dup = ArrayUtils.has_duplicates([1, 2, 3, 4])
# Returns False

# Check if sorted
is_sorted = ArrayUtils.is_sorted([1, 2, 3, 4])
# Returns True

is_desc = ArrayUtils.is_sorted([4, 3, 2, 1], ascending=False)
# Returns True
```

## Complete Function Reference

### Array Manipulation
- `reverse(arr, start=None, end=None)` - Reverse array or portion
- `rotate_right(arr, k)` - Rotate array right by k positions
- `rotate_left(arr, k)` - Rotate array left by k positions
- `move_zeros_to_end(arr)` - Move all zeros to end

### Searching
- `binary_search(arr, target)` - Standard binary search
- `binary_search_leftmost(arr, target)` - Find leftmost occurrence
- `binary_search_rightmost(arr, target)` - Find rightmost occurrence
- `two_sum_indices(arr, target)` - Find two indices that sum to target

### Two-Pointer Operations
- `two_pointer_partition(arr, val)` - Remove all occurrences of val
- `remove_duplicates_sorted(arr)` - Remove duplicates from sorted array
- `find_intersection_sorted(arr1, arr2)` - Find intersection of two sorted arrays
- `find_union_sorted(arr1, arr2)` - Find union of two sorted arrays

### Validation
- `has_duplicates(arr)` - Check if array has duplicates
- `is_sorted(arr, ascending=True)` - Check if array is sorted

### Transformation
- `prefix_sum(arr)` - Calculate prefix sum array
- `prefix_product(arr)` - Calculate prefix product array

### Advanced Algorithms
- `sliding_window_max(arr, k)` - Maximum in each sliding window
- `kadane_max_subarray(arr)` - Maximum sum of contiguous subarray

### Matrix Operations
- `flatten_2d_array(matrix)` - Flatten 2D array to 1D
- `transpose_matrix(matrix)` - Transpose a matrix

## Convenience Functions

For quick imports, the module also provides standalone convenience functions:

```python
from array_utils import reverse_array, rotate_array, binary_search, two_sum

# Use without ArrayUtils prefix
arr = [1, 2, 3, 4, 5]
reverse_array(arr)

rotate_array(arr, 2, direction='right')

index = binary_search([1, 2, 3, 4], 3)

indices = two_sum([2, 7, 11, 15], 9)
```

## Running Tests

A comprehensive test suite is included in `test_array_utils.py`:

```bash
python test_array_utils.py
```

All functions are thoroughly tested with edge cases including:
- Empty arrays
- Single element arrays
- Arrays with duplicates
- Large k values for rotation
- Boundary conditions

## Use Cases

These utilities are particularly useful for:
- **LeetCode Problems**: Quickly implement common patterns
- **Interview Preparation**: Focus on problem-solving, not implementation details
- **Competitive Programming**: Reusable tested functions
- **Learning**: Well-documented examples of common algorithms

## Related LeetCode Problems

This utility module can help solve many LeetCode problems, including:
- Two Sum (#1)
- Remove Duplicates from Sorted Array (#26)
- Remove Element (#27)
- Search in Rotated Sorted Array (#33)
- Maximum Subarray (#53)
- Rotate Array (#189)
- Move Zeroes (#283)
- Intersection of Two Arrays II (#350)
- Sliding Window Maximum (#239)
- And many more!

## Contributing

Feel free to add more utility functions following the same pattern:
1. Add the function to the `ArrayUtils` class
2. Include comprehensive docstring with examples
3. Add corresponding tests in `test_array_utils.py`
4. Update this README with the new function

## License

This code is provided as-is for educational and problem-solving purposes.

def binary_search(arr, target):
  """Executes a binary search on an array (that is sorted) and finds the target value.

  Args:
    arr: A sorted list of integers.
    target: The value to search.

  Returns:
    The index of the target value in the array,
        or "-1", if not found.
  """

  low = 0
  high = len(arr) - 1

  while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1

  return -1  


my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value = 23

result = binary_search(my_list, target_value)

if result != -1:
  print(f"Target is present at index {result}")
else:
  print("Target is not present in list")

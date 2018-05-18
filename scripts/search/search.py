




def linear_search(arr, key):
    for n in arr:
        if n == key:
            return True
    return False


# Only works for sorted arrays
def binary_search(nums, key):
    low  = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2 # take average midpoint. 
        if nums[mid] == key:
            return True
        elif key < nums[mid]:
                high = mid - 1
        else:
            low = mid + 1
    return False

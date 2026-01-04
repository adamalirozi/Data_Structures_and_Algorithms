"""
Given an integer array nums, find the subarray with the largest sum,
and return its sum.
"""
def maxSubarraySum(arr):
    """
    Docstring for maxSubarraySum
    
    :param arr: Description
    """
    res = arr[0]
  
    # Outer loop for starting point of subarray
    for i in range(len(arr)):
        currSum = 0
      
        # Inner loop for ending point of subarray
        for j in range(i, len(arr)):
            currSum = currSum + arr[j]
          
            # Update res if currSum is greater than res
            res = max(res, currSum)
          
    return res

if __name__ == "__main__":
    arr = [1, -2, 3, 4, 5, -1, -5, 10, 11, -1, -7, 6, -6]
    print(maxSubarraySum(arr))
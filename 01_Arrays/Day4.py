"""
Given an array nums of n integers, return an array of all the 
unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] = target
"""

def fourSum(arr, target):
    """
    Docstring for fourSum
    
    :param arr: Description
    :param target: Description
    """
    res = []
    n = len(arr)

    # Generating all possible quadruplets
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        curr = [arr[i], arr[j], arr[k], arr[l]]
                        
                        # Sort as needed in the output
                        curr.sort()  

                        # Making sure that all quadruplets with target
                        # sum are distinct
                        if curr not in res:
                            res.append(curr)
    return res

if __name__ == "__main__":
	arr = [10, 2, 3, 4, 5, 7, 8]
	target = 23
	print(fourSum(arr, target))
	
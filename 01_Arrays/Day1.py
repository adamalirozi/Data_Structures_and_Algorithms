"""
Given an array of integers and an integer target,
return indices of the two numbers such that they add up to target.
"""

def get_indices(arr, target):
    """
    Docstring for get_indices
    
    :param arr: Description
    :param target: Description
    """
    indices = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                indices.append((i,j))
    return indices

if __name__ == "__main__":
    arr = [2,1,3,7,8,6,9,4,10,12,18]
    target = 20
    print(get_indices(arr,target))
"""
DESCRIPTION:
Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

POINTERS: Use three pointers (e.g., low, mid, high) to track the boundaries of these zones.
ITERATION: Move through the array with the mid pointer

SWAPPING LOGIC:
- If you find a 0 (red) at I: Move tmid, swap it with the element at low and 
    advance both low and mid, placing the 0 in the red zone.
- If you find a 1 (white) at mid, it's already in the right potential area, so just advance mid.
- If you find a 2 (blue) at mid, swap it with the element at high and move high inward, 
    pushing the 2 to the blue zone, but don't advance mid yet, as the swapped element needs checking
"""


def SortColors(arr):
    """
    Docstring for SortColors
    
    :param arr: Description
    """
    low, mid = 0, 0
    high = len(arr)-1

    while mid <= high:
        # swap the element at mid with the element at low and 
        # advancing both low and mid
        if arr[mid] == 0:
            arr[mid],arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1
        # the element at mid is already in the right potential area, 
        # so just advancing mid
        elif arr[mid] == 1:
            mid += 1
        # swap the element at mid with the element at high and move high inward, 
        # pushing the 2 to the blue zone, but don't advance mid yet, 
        # as the swapped element needs checking
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
if __name__ == "__main__":
    arr = [2,0,2,1,1,0]
    print(SortColors(arr))
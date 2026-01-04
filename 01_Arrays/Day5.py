"""
Given an array of intervals where intervals[i] = [starting, ending], 
merge all overlapping intervals, and return an array of the non-overlapping 
intervals that cover all the intervals in the input

SORTING: The first step usually involves sorting the given intervals based on their starting points. 
This organization makes it efficient to check each interval against the next one in the sequence.

MERGING AND ITERATION: You must then iterate through the sorted list, comparing consecutive intervals. 
If an overlap is detected (meaning the start of the next interval falls before or within the end of the current one), 
you need to merge them by extending the end point of the current interval to the maximum end point of the overlapping pair. 
You continue this process, adding the final, merged intervals to your result list as you go
"""

def mergeOverlap(arr):
    """
    Docstring for mergeOverlap
    
    :param arr: Description
    """
    
    # Sort intervals based on start values
    arr.sort()

    res = []
    res.append(arr[0])

    for i in range(1, len(arr)):
        last = res[-1]
        curr = arr[i]

        # If current interval overlaps with the last merged
        # interval, merge them 
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)

    return res

if __name__ == "__main__":
    arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
    print(mergeOverlap(arr))
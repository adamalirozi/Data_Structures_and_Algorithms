"""
Given two strings s1 and s2, return true if s2 contains a permutation
of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
"""

from collections import Counter

def check_inclusion(s1: str, s2: str) -> bool:
    """
    Checks if s2 contains a permutation of s1 as a substring.

    This function uses a sliding window approach with frequency maps. It first
    calculates the character frequency of s1. Then, it slides a window of the
    same length across s2, comparing the window's character frequencies to those
    of s1 at each position.

    Args:
        s1: The shorter string to check permutations of.
        s2: The longer string to search within.

    Returns:
        True if s2 contains a permutation of s1, False otherwise.
    """
    # Optimization: if s1 is longer than s2, no permutation can exist as a substring.
    if len(s1) > len(s2):
        return False

    # 1. Create frequency maps for s1 and the initial window of s2
    # Counter(s1) creates a dictionary of char counts: e.g., "ab" -> {'a': 1, 'b': 1}
    s1_counts = Counter(s1)
    # Initialize the window counts with the first len(s1) characters of s2
    window_counts = Counter(s2[:len(s1)])

    # 2. Iterate through s2 using a sliding window
    # The loop runs from index 0 up to the point where a full window can still start
    for i in range(len(s2) - len(s1) + 1):
        # Check if the current window's character counts match s1's counts
        if s1_counts == window_counts:
            return True

        # Slide the window to the right for the next iteration:
        # a. If not the last iteration, add the new rightmost character
        if i + len(s1) < len(s2):
            new_char = s2[i + len(s1)]
            window_counts[new_char] += 1
            
            # b. Remove the leftmost character that just left the window
            old_char = s2[i]
            window_counts[old_char] -= 1
            # Optimization: remove char from map if its count drops to zero to keep maps clean for comparison
            if window_counts[old_char] == 0:
                del window_counts[old_char]

    # If the loop finishes without finding a match
    return False

# Example usage:
s1_example1 = "ab"
s2_example1 = "eidbaooo"
print(f"Can '{s2_example1}' contain a permutation of '{s1_example1}'? {check_inclusion(s1_example1, s2_example1)}")

s1_example2 = "ab"
s2_example2 = "eidboaoo"
print(f"Can '{s2_example2}' contain a permutation of '{s1_example2}'? {check_inclusion(s1_example2, s2_example2)}")

s1_example3 = "hello"
s2_example3 = "ooolleoooleh"
print(f"Can '{s2_example3}' contain a permutation of '{s1_example3}'? {check_inclusion(s1_example3, s2_example3)}")

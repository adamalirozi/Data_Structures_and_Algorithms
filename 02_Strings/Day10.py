"""
Given two strings s and t of lengths m and n respectively, return the minimum
window Substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty string "".
"""
from collections import Counter

def min_window_substring(s: str, t: str) -> str:
    """
    Finds the minimum window substring of s that contains every character in t.

    Args:
        s: The source string.
        t: The target string of characters to find.

    Returns:
        The minimum window substring, or "" if no such substring exists.
    """
    if not t:
        return ""

    # Count the frequency of each character in t
    target_counts = Counter(t)
    
    # Track the characters needed to fulfill the condition
    # `missing_count` will track how many characters from `t` are still missing in the current window
    missing_count = len(t)
    
    left = 0
    min_window_length = float('inf')
    min_window_start = 0

    # Iterate through the source string s with the right pointer
    for right, char_right in enumerate(s):
        # If the current character is needed for t
        if char_right in target_counts:
            # If we still need this specific character (count > 0 in the window context)
            if target_counts[char_right] > 0:
                missing_count -= 1
            # Decrement its count in our *needed* tracker. 
            # If it goes negative, it means we have extra instances, which is fine.
            target_counts[char_right] -= 1
            
        # Check if we have found all characters in the current window
        while missing_count == 0:
            # Update the minimum window size if the current one is smaller
            current_window_length = right - left + 1
            if current_window_length < min_window_length:
                min_window_length = current_window_length
                min_window_start = left
                
            # Now, try to contract the window from the left (move 'left' pointer)
            char_left = s[left]
            
            # If the character being removed from the left is one needed for t
            if char_left in target_counts:
                target_counts[char_left] += 1
                # If the count becomes positive again, it means we now *need* this 
                # character back in the window to maintain validity
                if target_counts[char_left] > 0:
                    missing_count += 1
            
            left += 1

    # If min_window_length is still infinity, no valid window was found
    if min_window_length == float('inf'):
        return ""
    
    # Return the minimum substring found
    return s[min_window_start : min_window_start + min_window_length]

# Example Usage:
s1 = "ADOBECODEBANC"
t1 = "ABC"
print(f"S: '{s1}', T: '{t1}'")
print(f"Minimum window: '{min_window_substring(s1, t1)}'") 
# Expected Output: "BANC"

s2 = "a"
t2 = "a"
print(f"\nS: '{s2}', T: '{t2}'")
print(f"Minimum window: '{min_window_substring(s2, t2)}'")
# Expected Output: "a"

s3 = "a"
t3 = "aa"
print(f"\nS: '{s3}', T: '{t3}'")
print(f"Minimum window: '{min_window_substring(s3, t3)}'")
# Expected Output: ""


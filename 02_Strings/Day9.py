"""
Given a string s, partition s such that every Substreing of the partition
is a Palindrome. Return all possible palindrome partitioning of s.
"""

from typing import List

def partition(s: str) -> List[List[str]]:
    """
    Given a string s, partition s such that every substring of the partition
    is a palindrome. Returns all possible palindrome partitioning of s.

    :param s: The input string.
    :return: A list of lists, where each inner list is a valid palindrome partition.
    """
    result = []
    current_partition = []
    n = len(s)

    def is_palindrome(sub: str) -> bool:
        """Helper function to check if a substring is a palindrome."""
        return sub == sub[::-1]

    def backtrack(start_index: int):
        """
        Recursive backtracking function to find all partitions.

        :param start_index: The index to start considering partitions from.
        """
        # Base case: If we have processed the entire string, add the current partition to the result.
        if start_index == n:
            result.append(current_partition[:]) # Append a copy
            return

        # Explore all possible substrings starting from start_index
        for end_index in range(start_index, n):
            substring = s[start_index : end_index + 1]
            if is_palindrome(substring):
                # If it's a palindrome, add it to the current partition
                current_partition.append(substring)
                # Recurse for the remaining part of the string
                backtrack(end_index + 1)
                # Backtrack: remove the last added substring to explore other possibilities
                current_partition.pop()

    backtrack(0)
    return result

# Example Usage:
input_str = "aab"
all_partitions = partition(input_str)
print(f"Input: '{input_str}'")
print(f"All Palindrome Partitions: {all_partitions}")

input_str_2 = "racecar"
all_partitions_2 = partition(input_str_2)
print(f"Input: '{input_str_2}'")
print(f"All Palindrome Partitions: {all_partitions_2}")

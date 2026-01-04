"""
Given a string s, sort it in decreasing order based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

COUNT OCCURRENCES: First, determine the number of times each unique character shows up in the given string.

ORDER BY FREQUENCY: Next, you must sort the characters themselves according to the counts you just calculated, 
arranging them from the most frequent to the least frequent.

CONSTRUCT THE RESULT: Finally, build a new output string by placing all instances of the characters in their new, frequency-sorted order
"""

# returns count of a character in the string
def countFrequency(s, ch):
    count = 0
    for i in range(len(s)):
        # check if current character matches ch
        if s[i] == ch:
            count += 1
    return count

# function to sort the string according to frequency
def frequencySort(s):
    n = len(s)

    # list to store frequency with corresponding character
    vp = []

    # insert frequency and character into the list
    for i in range(n):
        vp.append((countFrequency(s, s[i]), s[i]))

    # sort the list by frequency (pair first value)
    vp.sort()

    # build the final answer string
    ans = ""
    for freq, ch in vp:
        ans += ch

    return ans

if __name__ == "__main__":
    s = "aliroziadam"
    print(frequencySort(s))
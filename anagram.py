
# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# def isAnagram(self, s, t):

def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

s = "anagram"
t = "nagaram"
# s = "rat"
# t = "car"


print(is_anagram(s, t))

def is_anagram_v2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if not char in count:
            return False
        count[char] -= 1
    for val in count.values():
        if val != 0:
            return False
    return True

print(is_anagram_v2(s, t))

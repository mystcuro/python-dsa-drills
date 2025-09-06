# Pomo_07_Solidify/practice.py
# GOAL: Reinforce hash map patterns by re-implementing Two Sum and solving a new problem.

#  1. RE-IMPLEMENT TWO SUM from MEMORY 
# CONCEPT: Solidify the hash map pattern by implementing it without looking at the solution.
# PROBLEM: Solve the "Two Sum" problem again.
print(" 1. RE-IMPLEMENT TWO SUM from MEMORY ")
def two_sum_from_memory(nums, target):
    num_to_index = {} # Maps a number to its index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

# INPUT
nums_list = [3, 3]
target_sum = 6
print(f"Input: nums={nums_list}, target={target_sum}")
print(f"Output: {two_sum_from_memory(nums_list, target_sum)}") # EXPECTED OUTPUT: [0, 1]
print("\n"*2)


#  2. NEW PROBLEM: VALID ANAGRAM 
# CONCEPT: Two strings are anagrams if they contain the same characters with the same frequencies.
# A hash map (or a Counter) is the perfect tool to check this.
# PROBLEM: Given two strings, `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.
print(" 2. NEW PROBLEM: VALID ANAGRAM ")
from collections import Counter

def is_anagram(s, t):
    # Anagrams must have the same length. This is a quick check.
    if len(s) != len(t):
        return False
    # Create frequency maps for both strings and compare them.
    # If the maps are identical, they are anagrams.
    return Counter(s) == Counter(t)

# INPUT
s1, t1 = "anagram", "nagaram"
s2, t2 = "rat", "car"
print(f"Input: s='{s1}', t='{t1}'")
print(f"Output: {is_anagram(s1, t1)}") # EXPECTED OUTPUT: True

print(f"\nInput: s='{s2}', t='{t2}'")
print(f"Output: {is_anagram(s2, t2)}") # EXPECTED OUTPUT: False
print("\n"*2)
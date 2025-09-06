# Pomo_07_Solidify/exercise.py
# Instructions:
# 1. Fill in the functions below.
# 2. Run this file to test your functions.

def contains_duplicate(nums):
    """
    GUIDANCE: Given a list of integers, return `True` if any value appears at least twice,
    and `False` if every element is distinct.
    HINT: Use a set to keep track of the numbers you've already seen. If you encounter a
    number that's already in the set, you've found a duplicate.
    """
    # Your code here
    

def group_anagrams(strs):
    """
    GUIDANCE: Given a list of strings, group the anagrams together.
    Return a list of lists.
    HINT: The key insight is that all anagrams of a word will become the same word if their letters are sorted.
    You can use a dictionary where the key is the sorted version of a word and the value is a list of its anagrams.
    Example: 'eat', 'tea', 'ate' all become 'aet' when sorted.
    """
    # Your code here
    

#  Test Cases 
print(" Testing contains_duplicate ")
list1 = [1, 2, 3, 1]
print(f"Input: {list1}, Output: {contains_duplicate(list1)}") # Expected: True
list2 = [1, 2, 3, 4]
print(f"Input: {list2}, Output: {contains_duplicate(list2)}") # Expected: False

print("\n Testing group_anagrams ")
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
# The order of the groups and words within groups doesn't matter for the solution.
print(f"Input: {strs1}, Output: {group_anagrams(strs1)}")
# Expected: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] (or similar grouping)
# Pomo_05_Superpowers_Pt2/exercise.py
# Instructions:
# 1. Import the necessary classes from the `collections` module.
# 2. Fill in the functions below.
# 3. Run this file to test your functions.

from collections import defaultdict, Counter # You may need deque as well

def group_by_first_letter(words):
    """
    GUIDANCE: Given a list of words, create a dictionary where keys are the first letter
    of a word and values are a list of words starting with that letter.
    HINT: Use a `defaultdict(list)`. This way, the default value for a new key will be an empty list.
    """
    # Your code here
    

def find_anagrams(word1, word2):
    """
    GUIDANCE: Given two words, determine if they are anagrams (contain the same letters
    with the same frequency).
    HINT: This is a classic use case for `Counter`. Two words are anagrams if their
    character frequency maps are identical.
    """
    # Your code here
    

#  Test Cases 
print(" Testing group_by_first_letter ")
word_list = ["apple", "ant", "banana", "bat", "cat"]
grouped = group_by_first_letter(word_list)
print(f"Input: {word_list}, Output: {dict(grouped)}")
# Expected: {'a': ['apple', 'ant'], 'b': ['banana', 'bat'], 'c': ['cat']}

print("\n Testing find_anagrams ")
print(f"Input: 'listen', 'silent', Output: {find_anagrams('listen', 'silent')}") # Expected: True
print(f"Input: 'hello', 'world', Output: {find_anagrams('hello', 'world')}")   # Expected: False
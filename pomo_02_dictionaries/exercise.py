# Pomo_02_Dictionaries/exercise.py
# Instructions:
# 1. Fill in the functions below.
# 2. Run this file to test your functions.

def merge_dictionaries(dict1, dict2):
    """
    GUIDANCE: Given two dictionaries, create a new dictionary that contains keys from both.
    If a key exists in both dictionaries, the value from the second dictionary (dict2) should be used.
    HINT: You can create a copy of the first dictionary and then update it with the second. The .copy() method and a loop will be useful.
    """
    # Your code here
    

def find_most_common_word(text):
    """
    GUIDANCE: Given a string of text, find the most frequently occurring word.
    The function should be case-insensitive.
    Return a tuple of (word, count).
    HINT: You'll need to split the text into words, convert them to lowercase, and then use the frequency counting pattern.
    """
    # Your code here


#  Test Cases 
print(" Testing merge_dictionaries ")
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
print(f"Input: {d1}, {d2}, Output: {merge_dictionaries(d1, d2)}") # Expected: {'a': 1, 'b': 3, 'c': 4}

print("\n Testing find_most_common_word ")
text1 = "Apple banana apple orange banana apple"
print(f"Input: '{text1}', Output: {find_most_common_word(text1)}") # Expected: ('apple', 3)
text2 = "The quick brown fox jumps over the lazy dog The dog was happy"
print(f"Input: '{text2}', Output: {find_most_common_word(text2)}") # Expected: ('the', 3)
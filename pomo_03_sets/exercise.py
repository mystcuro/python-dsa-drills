# Pomo_03_Sets/exercise.py
# Instructions:
# 1. Fill in the functions below.
# 2. Run this file to test your functions.

def find_unique_elements(list1, list2):
    """
    GUIDANCE: Given two lists, return a new list containing elements that are present in
    either of the lists, but not in both.
    HINT: This is called the "symmetric difference". You can achieve this using set operations.
    Convert the lists to sets and use the `^` operator or the `.symmetric_difference()` method.
    """
    # Your code here
    

def has_all_vowels(sentence):
    """
    GUIDANCE: Given a sentence (string), determine if it contains all five vowels (a, e, i, o, u),
    case-insensitively.
    HINT: Create a set of the vowels found in the sentence and compare it to a target set of all vowels.
    """
    # Your code here
    

#  Test Cases 
print(" Testing find_unique_elements ")
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
# Sort the result to have a predictable order for testing
result1 = sorted(find_unique_elements(l1, l2))
print(f"Input: {l1}, {l2}, Output: {result1}") # Expected: [1, 2, 5, 6]

print("\n Testing has_all_vowels ")
sentence1 = "The quick brown fox jumps over the lazy dog"
print(f"Input: '{sentence1}', Output: {has_all_vowels(sentence1)}") # Expected: True
sentence2 = "This is a simple test"
print(f"Input: '{sentence2}', Output: {has_all_vowels(sentence2)}") # Expected: False
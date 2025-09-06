# Pomo_04_Superpowers_Pt1/exercise.py
# Instructions:
# 1. Fill in the functions below.
# 2. Run this file to test your functions.

def get_long_words(sentence):
    """
    GUIDANCE: Given a sentence, return a list of all words that have more than 4 letters.
    Use a list comprehension.
    HINT: Split the sentence into words first.
    """
    # Your code here
    

def sort_by_last_letter(words):
    """
    GUIDANCE: Given a list of words, sort them alphabetically by their last letter.
    HINT: Use a lambda function with the .sort() method's key argument. A word's last letter is at index -1.
    """
    # Your code here
    # Note: .sort() modifies the list in place, so you can just modify the list and not return anything.
    # For testing, it's often easier to return the sorted list. We will do that here.
    

#  Test Cases 
print(" Testing get_long_words ")
sentence1 = "The quick brown fox jumps over the lazy dog"
print(f"Input: '{sentence1}', Output: {get_long_words(sentence1)}")
# Expected: ['quick', 'brown', 'jumps']

print("\n Testing sort_by_last_letter ")
words1 = ["apple", "banana", "fig", "kiwi", "cherry"]
print(f"Input: {words1}, Output: {sort_by_last_letter(words1)}")
# Expected: ['banana', 'apple', 'fig', 'kiwi', 'cherry']
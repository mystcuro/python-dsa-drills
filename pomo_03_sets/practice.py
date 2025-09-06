# Pomo_03_Sets/practice.py
# GOAL: Understand the power of O(1) membership testing and uniqueness.

#  1. CREATION & UNIQUENESS 
# CONCEPT: Sets are unordered collections of unique elements.
# PROBLEM: Create a set from a list containing duplicates.
print(" 1. CREATION & UNIQUENESS ")
numbers_with_duplicates = [1, 2, 2, 3, 4, 3, 5]
unique_numbers = set(numbers_with_duplicates)
print(f"Original list: {numbers_with_duplicates}")
print(f"Set from list: {unique_numbers}") # EXPECTED OUTPUT: {1, 2, 3, 4, 5} (order may vary)
print("\n"*2)


#  2. MEMBERSHIP TESTING (THE SUPERPOWER) 
# CONCEPT: Checking if an item is 'in' a set is extremely fast (O(1)). This is much faster than checking for membership in a list (O(n)).
# PROBLEM: Use a set to efficiently find the first duplicate in a list.
print(" 2. MEMBERSHIP TESTING ")
numbers = [1, 5, 2, 8, 5, 3, 9, 2]
seen = set()
first_duplicate = None

for num in numbers:
    if num in seen:
        first_duplicate = num
        break # Stop as soon as we find the first one
    seen.add(num)

print(f"List to check: {numbers}")
print(f"First duplicate found: {first_duplicate}") # EXPECTED OUTPUT: 5
print("\n"*2)


#  3. ADD, REMOVE, DISCARD 
# CONCEPT: .remove() raises an error if the item is not found. .discard() does not.
# PROBLEM: Practice adding and removing elements from a set.
print(" 3. ADD, REMOVE, DISCARD ")
my_set = {10, 20, 30}
print(f"Original set: {my_set}")
my_set.add(40)
print(f"After adding 40: {my_set}")

my_set.remove(20)
print(f"After removing 20: {my_set}")

# This would cause an error: my_set.remove(99)
my_set.discard(99) # Does nothing, no error
print(f"After discarding 99 (no change): {my_set}")
print("\n"*2)


#  4. SET OPERATIONS 
# CONCEPT: Sets support mathematical operations like union, intersection, and difference.
# PROBLEM: Find common and unique items between two sets.
print(" 4. SET OPERATIONS ")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union = set_a.union(set_b)          # or set_a | set_b
intersection = set_a.intersection(set_b) # or set_a & set_b
difference = set_a.difference(set_b)     # or set_a - set_b

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union (all unique items from both): {union}")         # EXPECTED: {1, 2, 3, 4, 5, 6}
print(f"Intersection (items in both): {intersection}") # EXPECTED: {3, 4}
print(f"Difference (items in A but not B): {difference}")   # EXPECTED: {1, 2}
print("\n"*2)
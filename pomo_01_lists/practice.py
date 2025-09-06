# Pomo_01_Lists/practice.py
# GOAL: Get comfortable with the most common list operations.

#  1. CREATION & ACCESS 
# CONCEPT: Lists are ordered, mutable collections of items.
# PROBLEM: Create a list and access its elements by index.
print("\n" * 2)
print("1. CREATION & ACCESS")
nums = [5, 2, 8, 1, 9, 4]
print(f"Original list: {nums}")
print(f"First element (index 0): {nums[0]}")  # EXPECTED OUTPUT: 5
print(f"Last element (index -1): {nums[-1]}") # EXPECTED OUTPUT: 4
print("\n" * 2)

#  2. SLICING 
# CONCEPT: Slicing extracts a sub-list. The syntax is list[start:end:step]. The 'end' index is not included.
# PROBLEM: Extract various sub-sections from the list.
print("2. SLICING")
print(f"From index 1 to 4 (exclusive): {nums[1:4]}") # EXPECTED OUTPUT: [2, 8, 1]
print(f"The first 3 elements: {nums[:3]}") # EXPECTED OUTPUT: [5, 2, 8]
print(f"The last 3 elements: {nums[-3:]}") # EXPECTED OUTPUT: [1, 9, 4]
print("\n" * 2)


#  3. MODIFYING (APPEND & POP) 
# CONCEPT: .append() adds to the end (O(1) - fast). .pop() removes from the end (O(1) - fast).
# PROBLEM: Add an element to the end and then remove it.
print("3. MODIFYING (APPEND & POP) ")
nums.append(7)
print(f"List after appending 7: {nums}") # EXPECTED OUTPUT: [5, 2, 8, 1, 9, 4, 7]
removed_item = nums.pop()
print(f"Removed item: {removed_item}") # EXPECTED OUTPUT: 7
print(f"List after popping: {nums}") # EXPECTED OUTPUT: [5, 2, 8, 1, 9, 4]
print("\n" * 2)


#  4. SORTING (IN-PLACE vs. NEW LIST) 
# CONCEPT: .sort() modifies the list in-place. sorted() returns a new, sorted list.
# PROBLEM: Sort a list using both methods to see the difference.
print("4. SORTING (IN-PLACE vs. NEW LIST) ")
nums_to_sort = [3, 1, 4, 1, 5, 9]
print(f"Original list to sort: {nums_to_sort}")
print("\n" * 2)
# Method 1: sorted() returns a new list
new_sorted_list = sorted(nums_to_sort)
print(f"New sorted list .sorted(list): {new_sorted_list}") # EXPECTED OUTPUT: [1, 1, 3, 4, 5, 9]
print(f"Original list is unchanged: {nums_to_sort}") # EXPECTED OUTPUT: [3, 1, 4, 1, 5, 9]

# Method 2: .sort() modifies the list in-place
nums_to_sort.sort()
print(f"Original list after .sort(): {nums_to_sort}") # EXPECTED OUTPUT: [1, 1, 3, 4, 5, 9]
print("\n" * 2)
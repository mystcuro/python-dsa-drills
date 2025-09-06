# Pomo_01_Lists/exercise.py
# Instructions:
# 1. Fill in the functions below.
# 2. Run this file to test your functions.

def get_middle_elements(input_list):
    """
    GUIDANCE: Given a list, return a new list containing only the two middle elements.
    If the list has an odd number of elements, return the single middle element.
    HINT: You'll need to calculate the middle index. Integer division `//` will be helpful.
    """
    #Your Code
    n = len(input_list)
    mid = n//2

    if n%2 == 0:
        return [input_list[mid-1], input_list[mid]]
    else:
        return input_list[mid]


def remove_evens(input_list):
    """
    GUIDANCE: Given a list of integers, return a new list with all even numbers removed.
    HINT: You can create an empty list and loop through the input list, appending only the odd numbers.
    """
    #Your Code
    result = []
    for num in input_list:
        if num%2!=0:
            result.append(num)
    return result

#  Test Cases 
print("Testing get_middle_elements")
list1 = [1, 2, 3, 4, 5, 6]
print(f"Input: {list1}, Output: {get_middle_elements(list1)}") # Expected: [3, 4]
list2 = [1, 2, 3, 4, 5]
print(f"Input: {list2}, Output: {get_middle_elements(list2)}") # Expected: [3]

print("\nTesting remove_evens()")
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Input: {list3}, Output: {remove_evens(list3)}") # Expected: [1, 3, 5, 7, 9]
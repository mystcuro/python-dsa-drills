# Pomo_06_Two_Sum/exercise.py
# Instructions:
# 1. Fill in the functions below.
# 2. Run this file to test your functions.

def two_sum_sorted(sorted_nums, target):
    """
    GUIDANCE: This is a variation of Two Sum where the input list is already sorted.
    You can solve this efficiently without a hash map using the "two-pointer" technique.
    HINT: Start with one pointer at the beginning of the list (`left`) and one at the end (`right`).
    - If `nums[left] + nums[right]` is too small, move the left pointer forward.
    - If it's too big, move the right pointer backward.
    - If they equal the target, you've found your pair!
    Return the 1-based indices, not 0-based.
    """
    # Your code here
    

#  Test Cases 
print(" Testing two_sum_sorted ")
nums1 = [2, 7, 11, 15]
target1 = 9
print(f"Input: {nums1}, {target1}, Output: {two_sum_sorted(nums1, target1)}") # Expected: [1, 2]

nums2 = [2, 3, 4]
target2 = 6
print(f"Input: {nums2}, {target2}, Output: {two_sum_sorted(nums2, target2)}") # Expected: [1, 3]
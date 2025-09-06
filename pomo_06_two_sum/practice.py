# Pomo_06_Two_Sum/practice.py
# GOAL: Integrate multiple concepts to solve a classic interview problem.

#  PROBLEM: TWO SUM 
# Given a list of integers `nums` and an integer `target`, return the indices
# of the two numbers such that they add up to `target`.
# You may assume that each input would have exactly one solution, and
# you may not use the same element twice.

#  1. BRUTE-FORCE APPROACH (O(n^2)) 
# CONCEPT: The simplest way is to check every pair of numbers.
# This uses nested loops, making it slow for large inputs (O(n^2) time complexity).
print(" 1. BRUTE-FORCE APPROACH ")
def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)): # j starts after i
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# INPUT
nums_list = [2, 7, 11, 15]
target_sum = 9
print(f"Input: nums={nums_list}, target={target_sum}")
print(f"Output (Brute-Force): {two_sum_brute_force(nums_list, target_sum)}") # EXPECTED OUTPUT: [0, 1]
print("\n"*2)


#  2. OPTIMAL APPROACH with HASH MAP (O(n)) 
# CONCEPT: We can trade space for time. By using a dictionary (hash map), we can
# find the needed "complement" in O(1) time. This reduces the total time complexity to O(n).
# For each number, we calculate `complement = target - number`.
# If the complement is already in our map, we've found a pair!
# If not, we add the current number and its index to the map for future checks.
print(" 2. OPTIMAL APPROACH with HASH MAP ")
def two_sum_optimal(nums, target):
    num_map = {} # Dictionary to store {number: index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            # We found the pair
            return [num_map[complement], i]
        # If complement not found, add the current number and its index to the map
        num_map[num] = i
    return []

# INPUT
nums_list_2 = [3, 2, 4]
target_sum_2 = 6
print(f"Input: nums={nums_list_2}, target={target_sum_2}")
print(f"Output (Optimal): {two_sum_optimal(nums_list_2, target_sum_2)}") # EXPECTED OUTPUT: [1, 2]
print("\n"*2)
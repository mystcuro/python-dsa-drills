# Pomo_04_Superpowers_Pt1/practice.py
# GOAL: Write more concise code with list comprehensions and custom sorting.

#  1. LIST COMPREHENSIONS 
# CONCEPT: A compact way to create lists from sequences. Syntax: [expression for item in iterable if condition]
# PROBLEM: Create a list of squares for numbers 0 through 9.
print(" 1. LIST COMPREHENSIONS ")

# Traditional way
squares_loop = []
for i in range(10):
    squares_loop.append(i * i)

# Comprehension way (preferred)
squares_comp = [i * i for i in range(10)]

print(f"Using a loop:     {squares_loop}")
print(f"Using comprehension: {squares_comp}") # EXPECTED OUTPUT: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print("\n"*2)


#  2. LIST COMPREHENSIONS with CONDITION 
# CONCEPT: You can add an 'if' clause to filter items.
# PROBLEM: From a list of numbers, create a new list containing only the even numbers, squared.
print(" 2. LIST COMPREHENSIONS with CONDITION ")
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
squared_evens = [n * n for n in numbers if n % 2 == 0]

print(f"Original numbers: {numbers}")
print(f"Squared evens: {squared_evens}") # EXPECTED OUTPUT: [4, 16, 36, 64]
print("\n"*2)


#  3. SORTING with a CUSTOM KEY (lambda) 
# CONCEPT: The `key` argument in sort() lets you specify a function to decide the sorting order.
# A `lambda` function is a small, anonymous function, perfect for this.
# PROBLEM: Sort a list of strings by their length, not alphabetically.
print(" 3. SORTING with a CUSTOM KEY (lambda) ")
words = ["apple", "banana", "fig", "kiwi", "cherry"]
print(f"Original words: {words}")

# Sort by length
words.sort(key=lambda word: len(word))

print(f"Words sorted by length: {words}") # EXPECTED OUTPUT: ['fig', 'kiwi', 'apple', 'cherry', 'banana']
print("\n"*2)


#  4. CUSTOM SORTING with TUPLES 
# CONCEPT: Sorting a list of complex objects like tuples or objects.
# PROBLEM: Sort a list of (name, age) tuples by age.
print(" 4. CUSTOM SORTING with TUPLES ")
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
print(f"Original people list: {people}")

# Sort by the second element of the tuple (age)
people.sort(key=lambda person: person[1])

print(f"People sorted by age: {people}") # EXPECTED OUTPUT: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
print("\n"*2)
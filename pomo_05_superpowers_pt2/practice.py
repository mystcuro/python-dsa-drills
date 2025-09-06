# Pomo_05_Superpowers_Pt2/practice.py
# GOAL: Learn the specialized tools from the `collections` module.

from collections import deque, defaultdict, Counter

#  1. DEQUE for EFFICIENT QUEUES 
# CONCEPT: Lists are slow for adding/removing from the beginning (O(n)). A `deque` (double-ended queue) is fast for both ends (O(1)).
# This is crucial for algorithms like Breadth-First Search (BFS).
# PROBLEM: Simulate a simple queue where people are added to the end and served from the front.
print(" 1. DEQUE for EFFICIENT QUEUES ")
line = deque(['Alice', 'Bob', 'Charlie'])
print(f"Initial line: {line}")

line.append('David') # David gets in line
print(f"After David arrives: {line}")

served_person = line.popleft() # Alice is served
print(f"Served: {served_person}, Remaining line: {line}") # EXPECTED: Served: Alice, Remaining line: deque(['Bob', 'Charlie', 'David'])
print("\n"*2)


#  2. DEFAULTDICT for SIMPLER FREQUENCY COUNTING 
# CONCEPT: A `defaultdict` provides a default value for a non-existent key, avoiding KeyErrors and simplifying code.
# PROBLEM: Refactor the frequency counting code from Pomo 2 using `defaultdict`.
print(" 2. DEFAULTDICT for SIMPLER FREQUENCY COUNTING ")
message = "hello world"

# With a regular dict, you need .get()
# char_counts = {}
# for char in message:
#     char_counts[char] = char_counts.get(char, 0) + 1

# With defaultdict, it's cleaner. `int` provides a default value of 0.
char_counts_dd = defaultdict(int)
for char in message:
    char_counts_dd[char] += 1

print(f"Frequency counts using defaultdict: {dict(char_counts_dd)}")
# EXPECTED: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
# Note: We wrap it in dict() for a cleaner printout.
print("\n"*2)


#  3. COUNTER - THE ULTIMATE FREQUENCY COUNTER 
# CONCEPT: `Counter` is a specialized dictionary subclass for counting hashable objects. It's the most efficient way to do frequency counts.
# PROBLEM: Count character frequencies in one line using `Counter`.
print(" 3. COUNTER ")
message = "hello world"
char_counts_counter = Counter(message)

print(f"Frequency counts using Counter: {char_counts_counter}")
# EXPECTED: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Counter has useful methods, like .most_common()
print(f"Two most common chars: {char_counts_counter.most_common(2)}") # EXPECTED: [('l', 3), ('o', 2)]
print("\n"*2)
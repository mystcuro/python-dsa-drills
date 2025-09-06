# Pomo_02_Dictionaries/practice.py
# GOAL: Master the frequency counting pattern and safe dictionary access.

# 1. CREATION & ACCESS 
# CONCEPT: Dictionaries store data in key-value pairs. Access is O(1) - very fast.
# PROBLEM: Create a dictionary representing a user and access its properties.

print("\n" * 2)
print("1. CREATION & ACCESS ")
user = {'username': 'coder123', 'email': 'coder@example.com', 'level': 5}
print(f"User dictionary: {user}")
print(f"Username: {user['username']}") # EXPECTED OUTPUT: coder123

# Accessing a non-existent key will raise a KeyError.
# print(user['word']) # This would cause an error.
print("\n" * 2)


# 2. SAFE ACCESS with .get() 
# CONCEPT: The .get() method safely retrieves a key's value. It returns a default value (or None) if the key doesn't exist, preventing errors.
# PROBLEM: Safely access a key that exists and one that doesn't.
print("2. SAFE ACCESS with .get() ")
email = user.get('email')
print(f"Email (safe access): {email}") # EXPECTED OUTPUT: coder@example.com

word = user.get('word', 'Not set') # Provide a default value
print(f"word (safe access): {word}") # EXPECTED OUTPUT: Not set
print("\n" * 2)


# 3. FREQUENCY COUNTING PATTERN 
# CONCEPT: This is a vital DSA pattern used to count occurrences of items in a sequence.
# PROBLEM: Count the frequency of each character in a string.
print("3. FREQUENCY COUNTING PATTERN ")
message = "hello world"
char_counts = {}

for char in message:
    # Use .get(key, 0) to handle the first time we see a character
    char_counts[char] = char_counts.get(char, 0) + 1

print(f"Character counts for '{message}': {char_counts}")
# EXPECTED OUTPUT: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
print("\n" * 2)

# 4. ITERATION
# CONCEPT: You can iterate over keys, values, or .items(). items() return key-value pairs.
# PROBLEM: Iterate through the user dictionary and print its contents in different ways.
print("4. ITERATION ")
print("Iterating over keys:")
for key in user.keys():
    print(f"  Key: {key}")

print("\nIterating over values:")
for value in user.values():
    print(f"  Value: {value}")

print("\nIterating over items (key-value pairs):")
for key, value in user.items():
    print(f"  {key}: {value}")
print("\n"*2)
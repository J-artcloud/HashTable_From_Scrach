# Custom Hash Table Implementation in Python

This repository contains a from-scratch implementation of a Hash Table data structure in Python, built to satisfy the requirements for the freeCodeCamp "Create a Hash Table" project.

The purpose of this project is to demonstrate key-value storage fundamentals, custom ASCII character summation hashing, nested dictionary bucket organization, collision handling, and fast lookup operations.

---

## FreeCodeCamp Project Conditions Passed

This implementation satisfies all required conditions defined by freeCodeCamp:

1. HashTable Class Structure: The `HashTable` class initializes an internal `collection` object to hold hash buckets.
2. Custom Hash Algorithm: The `hash(string)` method processes string keys by summing the ASCII integer values of each character using `ord()`.
3. Insertion Method: The `add(key, value)` method inserts key-value pairs into the table and updates existing keys if they already exist.
4. Removal Method: The `remove(key)` method safely deletes a specific key-value pair from its assigned hash bucket.
5. Search & Retrieval Method: The `lookup(key)` method searches for a key and returns its corresponding value, or `None` if the key does not exist.
6. Collision Handling: Handles identical hash codes (such as anagram keys) by nesting keys inside secondary dictionary buckets under their shared hash key.

---

## How This Implementation Works

### 1. ASCII Hashing Algorithm
The internal `hash` method iterates through every character in a string key, converts the character to its ASCII integer equivalent using Python's built-in `ord()` function, and sums these values together:

  hash_code = sum of ord(char) for each char in key

Example calculation for `'golf'`:
- `'g'` = 103
- `'o'` = 111
- `'l'` = 108
- `'f'` = 102
- Total `hash_code` = 424

### 2. Collision Handling with Anagrams
Because this hash function sums character values, words that share identical letters in different orders (anagrams) produce identical hash codes:

- `'read'` -> 114 + 101 + 97 + 100 = 412
- `'dear'` -> 100 + 101 + 97 + 114 = 412

To resolve collisions without overwriting data, `self.collection` uses a two-tiered dictionary structure:
- **Outer Dictionary**: Maps the computed integer `hash_code` to a bucket.
- **Inner Dictionary (Bucket)**: Maps the actual string `key` to its `value`.

Example state of `self.collection` after inserting `'read'` and `'dear'`:

  {
      424: {'golf': 'sport'},
      412: {
          'read': 'book',
          'dear': 'friend'
      },
      441: {'rose': 'flower'}
  }

---

## Code Methods Overview

* `__init__()`
  Initializes `self.collection` as an empty dictionary `{}` to store all buckets.

* `hash(string: str)`
  Calculates and returns the integer ASCII sum of the input string.

* `add(key, value)`
  Calculates the key's `hash_code`. Creates an inner dictionary at `self.collection[hash_code]` if it does not exist yet, then sets `self.collection[hash_code][key] = value`.

* `remove(key)`
  Computes the `hash_code` and verifies that both the hash bucket and key exist before executing `del self.collection[hash_code][key]`.

* `lookup(key)`
  Computes the `hash_code`, retrieves the associated bucket, and checks for the key inside that bucket. Returns the matching value if found, otherwise returns `None`.

---

## Usage Example

```python
from main import HashTable

# Instantiate the table
ht = HashTable()

# Compute an ASCII hash value
print(ht.hash('golf'))  # Output: 424

# Add key-value pairs
ht.add('golf', 'sport')
ht.add('read', 'book')
ht.add('dear', 'friend')  # Collides with 'read' at hash code 412

# Look up values
print(ht.lookup('golf'))  # Output: sport
print(ht.lookup('read'))  # Output: book
print(ht.lookup('dear'))  # Output: friend

# Remove a key-value pair
ht.remove('read')
print(ht.lookup('read'))  # Output: None

# Inspect internal collection state
print(ht.collection)

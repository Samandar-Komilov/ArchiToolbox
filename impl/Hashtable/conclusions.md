# Hashtable Conclusions

A hash table (aka hash map or dictionary) is a data structure that stores key-value pairs and supports:
- Insert (put)
- Lookup (get)
- Delete
Average complexity: `O(1)`, thanks to a hash function that maps keys to indices.

**Hash Function.** We need a way to map a key to the array index. Hash function helps in this scenario. The simplest hash function:
- `hash(key) = key % size`

**Collisions.** The following methods exist to handle collisions:
- Chaining (linked list)
- Open Addressing
    - Linear Probing
    - Quadratic Probing
    - Double Hashing
Now we'll see each of the methods and implement in Python.

**Load Factor.** `n / m` where `n` = number of keys, `m` = table size. High load factor -> rehashing through resizing. This is required when you use linear or quadratic probing, as high load factor causes to the repeated probes and even infinite loop.
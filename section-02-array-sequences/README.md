# Array Sequences
### Python Classes
- List: [1,2,3]
- Tuple: (1,2,3)
- String: '123'

All sequences support indexing

# Low Level Arrays
### How computers store information:
- computer memory
- memory address
- units of memory (bit and bytes)
- memory retrieval

### Low-level computer architecture
- memory of computer stored in bits
- a unit is byte, which is 8 bits
- each byte is associated with unique address

### Arrays
- computer main memory performs random access memory (RAM)
- individual byte of memory can be stored or retrieved in O(1) time
- programming language keeps track of the association between an identifier and the memory address
- a text string is stored as ordered sequence of individual characters
- Python internally represents *each unicode chracter with 16 bits (i.e., 2 bytes)*

# Python Array Concepts

### Array Vocabulary
- an array contains a sequence of **characters**
- each location in an array is a **cell**
- integer **index** describe location in array

### Array memory allocation
- each cell in array uses samee number of bytes
- any cell can be accessed in constant time
- memory address can be computed as: **start + (cellsize)(index)**

### Referential Arrays
- each element is a **reference** to the object
- a single list instance may include multiple references to the same object as elements of the list
- single object can be an element of two or more lists
- computing a slice of a list results in a new list instance
    * new list has references to the same elements found in original list
- ```backup = list(primes)```
    * produces new list that is a **shallow copy** which references same elements as first list
    * if contents in list are immutable type, a **deep copy**, or a new list with new elements can be produced by using deepcopy function from the copy module
- ```counters = [0] * 8```
    * all eight cells reference the same object
- ```counters[2] += 1```
    * technically, does not change the value of the existing integer instance
    * this computes a new integer
- ```primes.extend(extras)```
    * adds references to a list
# Stacks, Queues, Deques (pronounced like "decks")
- linear structures
- similar to arrays, but each of these structures differs by how it adds and removes items

# Stacks Overview
- stack: an ordered collection of items where the addition of new items and removal of existing items always takes place at the same end
- top: the end of a stack where addition and removal occurs
- base: the end opposite the top
- last-in first-out (LIFO) ordering principle
    * provides ordering based on length of time in the collection
    * newer items near top, older near the base
- first items are "pushed" to the stack beginning at base, and as items are "popped" out
- computer science fundamentals, stacks can reverse the order of items
- order of insertion is the reverse of the order of removal

# Queue Overview
- queue: an ordered collection of items where addition of new items happens at one end (rear/back -> enqueue), and the removal of existing items occurs at the other end (front -> dequeue)
- as element enters queue, it starts at the read and makes its way toward the front, until it is the next element to be removed
- first-in first-out (FIFO) ordering principle, aka "first-come first-served"
- example: waiting in line to get order from restaurant
- enqueue: add a new item to the rear of the queue
- dequeue: removing the front item from the queue

# Deque Overview
- aka double-endedd queue, is an ordered collection of items similar to the queue
- has two ends, front and rear, and the items remain positioned in the collection
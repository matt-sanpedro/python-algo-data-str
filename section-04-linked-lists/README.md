# Linked Lists Topics
- singly linked lists
- implementation of singly linked list
- doubly linked lists
- implementation of a doubly linked list
- interview problems

# Singly Linked List

## Overview
- collection of nodes that collectively form a linear sequence
- each node stores a reference to an object that is an element of the sequence
- each node has a reference to the next node of the list

## Implementation
- a list instance maintains a member named head that identifies the first node of the list
- some applications include member tail that identifies the last node of the list
- tail node can be identified as having None as its next reference
- traversing the linked list means going through the head to tail of the linked list
    * link or pointer is the next reference of a node
    * traversing is synonymous with link hopping or pointer hopping
- each node is represented as a unique object
    * an instance stores a reference to its element and reference to next node

## Inserting an Element at the Head
- linked list does not have a predetermined fixed size
- space ios used proportionally to its current number of elements
- to insert a new element at the head of the list:
    * create a new node
    * set its element to the new element
    * set its next link to refer to the current head
    * set list's head to point to new node

## Inserting an Element at the Tail
- implement by keeping a reference to the tail node
    * create new node
    * assign next reference to None
    * set the next reference of the tail to point to this new node
    * update tail reference itself to this new node

## Removing an Element
- removing element from head is essentially the reverse operation of inserting a new element at the head
- cannot easily delete the last node of a singly linked list
    * must be able to access node before the last node in order to remove last node
    * cannot reach node before tail by following next links from the tail
    *  to support operation efficiently, need to make our list "doubly linked"
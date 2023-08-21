'''
Fibonnaci Sequence\
In this interview excercise we will begin to get a feel of having to solve a single problem multiple ways!

## Problem Statement
Implement a [Fibonnaci Sequence](https://en.wikipedia.org/wiki/Fibonacci_number) in three different ways:

* Recursively
* Dynamically (Using Memoization to store results)
* Iteratively
___
#### Function Output
Your function will accept a number **n** and return the **nth** number of the fibonacci sequence
___
Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off with a base case checking to see if n = 0 or 1, then it returns 1. 

Else it returns fib(n-1)+fib(n+2).
'''
def fib_rec(n):
    if n==0 or n==1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

print(fib_rec(10))
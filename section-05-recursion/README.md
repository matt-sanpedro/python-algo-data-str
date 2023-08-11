# Recursion

### Topics Covered
1. Overview of Recursion
2. Basic Recursion Examples
3. Introduction to Memoization and Dynamic Programming
4. Four real interview questions

### What is Recursion?
Two main instances:
1. Technique in which a function makes one or more calls to itself
2. Data structure uses smaller instances of exact same type of data structure when it represents itself

### Why use Recursion?
- powerful alternative for performing repetitions of tasks in which a loop is not ideal
- most modern programming languages support recursion
- recursion serves as a great tool for building out particular data structures

## Factorial Example
- explain recursion through example exercise of creating factorial function
- factorial function is denoted with an exclamation point and is defined as product of integers from 1 to n
- $$ n! = n * (n - 1) * (n - 2) ... 3 * 2 * 1 $$
    * `if n = 0, then n! = 1`
- $$ 4! = 4 * 3 * 2 * 1 = 24 = 4 * (3 * 2 * 1) = 4 * (3!) $$
- concept of __base case__ to express factorial in recursive manner
- $$ n! = n * (n - 1)! $$
    * `if n = 0, then n! = 1`
    * __base case__ occurs once `n = 0`
    * recursive cases are defined by equation
- on the factorial of zero (0!) defined to be equal to 1
    * $$ 0! = 1! = 1 $$

### Important Recursion Hint
- for recursive solution, think about base case
- solution return base case once all resursive cases have been worked through

'''
Balanced Parentheses Check 

Problem Statement:
Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. Assume that the string doesn’t contain any other character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not. 

Note: You can assume the input string has no spaces.
'''
# SOLUTION 1: O(n)
def balance_check(s):
    # initialize counter
    count = 0

    for char in s:
        # print(char)
    
        if char in ['(', '{', '[']:
            count += 1
        elif char in [')', '}', ']']:
            count -= 1

    return count==0

# print(balance_check('[]'))
# print(balance_check('[](){([[[]]])}'))
# print(balance_check('()(){]}'))

# SOLUTION 2: Stacks
def balance_check2(s):
    # edge case: if even number of brackets
    if len(s)%2 != 0:
        return False

    opening = set('([{')
    # print(opening)
    matches = set([ ('(', ')'), ('[',']'), ('{','}') ])
    # print(matches)
    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()

            if (last_open,paren) not in matches:
                return False

    return len(stack)==0

print(balance_check('([)]'))
print(balance_check2('([)]'))
# print(balance_check2('[]'))
# print(balance_check2('[](){([[[]]])}'))
# print(balance_check2('()(){]}'))
'''
Balanced Parentheses Check 

Problem Statement:
Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. Assume that the string doesn’t contain any other character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not. 

Note: You can assume the input string has no spaces.
'''
# SOLUTION 1: O(n)
def balance_check(s):
    # initialize counters
    square_count = 0
    paren_count = 0
    curly_count = 0

    for char in s:
        # print(char)
        if '[' in char:
            square_count += 1
        elif ']' in char: 
            square_count -= 1
        elif '(' in char: 
            paren_count += 1
        elif ')' in char: 
            paren_count -= 1
        elif '{' in char: 
            curly_count += 1
        elif '}' in char: 
            curly_count -= 1

    if square_count==0 and paren_count==0 and curly_count==0:
        return True
    else:
        return False


# print(balance_check('[]'))
# print(balance_check('[](){([[[]]])}'))
# print(balance_check('()(){]}'))

def balance_check2(s):
    pass
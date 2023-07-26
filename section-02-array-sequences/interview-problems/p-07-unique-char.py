'''
PROBLEM STATEMENT:
Given a string,determine if it is comprised of all unique characters. 
For example, the string 'abcde' has all unique characters and should return True. 
The string 'aabcde' contains duplicate characters and should return false.
'''
# SOLUTION 1: Storing unique values in a list
def uni_char(s):
    # edge case: string has zero or one character
    if len(s)==0 or len(s)==1:
        return True
    
    char_list = []

    for char in s:
        if char in char_list:
            return False
        else:
            char_list.append(char)

    return True

# print(uni_char('abcdefg'))


# SOLUTION 2: Python sets with the length function
def uni_char2(s):
    return len(set(s)) == len(s)


# SOLUTION 3: Storing unique values in a set
def uni_char3(s):
    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)

    return True

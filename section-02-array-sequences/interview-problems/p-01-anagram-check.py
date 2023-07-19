'''
Anagram Check Problem Statement:
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word). 

For example:

    "public relations" is an anagram of "crap built on lies."
    
    "clint eastwood" is an anagram of "old west action"
    
**Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".**
'''
# Solution 1: using the sorted method with replace
def anagram(s1, s2):   
    s1_sort = sorted(s1.replace(" ",""))
    s2_sort = sorted(s2.replace(" ",""))

    return s1_sort == s2_sort

# print(anagram('dog','god'))
# print(anagram('clint eastwood','old west action'))
# print(anagram('aa','bb'))

# Solution 2: counting the letters with dictionaries (more manual)
def anagram2(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    # edge case check
    if len(s1) != len(s2):
        return False

    count = {}

    # first count by adding the s1 character occurences
    for letter in s1:
        if not check_key(count,letter):
            # condition 1: initialize the key since it DNE
            count[letter] = 1
        else:
            # condition 2: key already exists so add 1 to the count "value"
            count[letter] += 1

    # print(count)

    for letter in s2:
        if not check_key(count,letter):
            # condition 1: initialize the key since it DNE -> also indicates NOT an anagram
            count[letter] = -1
            print('Additional letter found: {}'.format(letter))
            return False
        else:
            # condition 2: key already exists so minus 1 to the count "value"
            count[letter] -= 1       

    # print(count)

    for key in count.keys():
        # print(key, count[key])
        if count[key] != 0:
            return False
    
    return True


def check_key(dic,key):
    if key in dic.keys():
        return True
    else:
        return False

print(anagram2('dog','god'))
print(anagram2('clint eastwood','old west action'))
print(anagram2('aa','bb'))
print(anagram2('dog','cat'))

'''
PROBLEM STATEMENT:
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space. 

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
'''
# SOLUTION 1: O(n) my solution
def compress(s):
    # edge case: no letters provided in string
    if len(s)==0:
        return ''

    # edge case: one letter provided in string
    if len(s)==1:
        return s+'1'

    # initial conditions
    letter_before = s[0]
    count = 1
    comp_string = ''


    for index, letter in enumerate(s[1:]):
        # print('Letter: {}, Count: {}'.format(letter, count))
        if (letter != letter_before) and (index+2==len(s)):
            comp_string += f'{letter_before}{count}'
            # on last index, get last letter in
            comp_string += f'{letter}1'
        elif (letter == letter_before) and (index+2==len(s)):
            # handle storing the last letter in the list
            # print('LAST Letter: {}, Count: {}'.format(letter, count))
            comp_string += f'{letter_before}{count+1}'
        elif (letter != letter_before):
            # do operations to store
            # print('Letter: {}, Count: {}'.format(letter, count))
            comp_string += f'{letter_before}{count}'
            # reset count to zero and letter before
            count = 1
            letter_before = letter
        else:
            # assume letter is still same and continue counting
            count += 1

    return comp_string

# SOLUTION 2: Instructor method - run/length compression algorithm
def compress2(s):
    r = ''
    l = len(s)

    # edge case: length of zero
    if l == 0:
        return ''

    # edge case: one letter in string
    if l == 1:
        return s+'1'
    
    # initial conditions
    count = 1
    i = 1

    while i < l:
        if s[i] == s[i-1]:
            count += 1
        else:
            r = r + s[i-1] + str(count)
            count = 1

        i += 1
    
    r = r + s[i-1] + str(count)

    return r
    
# compress('')
# compress('AABBCC')
# compress('AAABCCDDDDD')
# compress('AABBC')
# print(compress('A'))

print(compress2('AAB'))
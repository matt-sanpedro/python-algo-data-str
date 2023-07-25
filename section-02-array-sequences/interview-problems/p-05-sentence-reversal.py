'''
PROBLEM STATEMENT:
Given a string of words, reverse all the words. For example:
'''
# SOLUTION 1: O(n)
def rev_word(s):
    clean_data = s.strip().split(' ')

    # reverse
    reversed = []

    for word in clean_data[::-1]:
        if len(word) != 0:
            # print(word)
            reversed.append(word)
    
    return ' '.join(reversed)

# SOLUTION 2: Manual Method with While loops
def rev_word2(s):
    words = []
    length = len(s)
    space = [' ']

    # index tracker
    i = 0

    while i < length:
        if s[i] not in space:
            word_start = i

            while i < length and s[i] not in space:
                i += 1
            words.append(s[word_start:i])

        i += 1
    return ' '.join(reversed(words))


# print(rev_word('Hi John,   are you ready to go?'))
# # OUTPUT: 'go? to ready you are John, Hi'
# print(rev_word('    space before'))
# print(rev_word('   Hello John    how are you   '))
# print(rev_word('1'))

print(rev_word2('Hi John,   are you ready to go?'))
# OUTPUT: 'go? to ready you are John, Hi'
print(rev_word2('    space before'))
print(rev_word2('   Hello John    how are you   '))
print(rev_word2('1'))

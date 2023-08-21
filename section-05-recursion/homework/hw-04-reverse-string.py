'''
Reverse a String

This interview question requires you to reverse a string using recursion. Make sure to think of the base case here.

Again, make sure you use *recursion* to accomplish this. **Do not slice (e.g. string[::-1]) or use iteration, there must be a recursive call for the function.**
'''
def reverse(s):
    # print('last letter: {}'.format(s[len(s)-1]))
    # print('up to last:  {}'.format)(s[0:len(s)-1])
    if len(s)==1:
        return s
    else:
        # return s[len(s)-1] + reverse(s[0:len(s)-1])
        return reverse(s[1:]) + s[0] 
    
print(reverse('hello world'))

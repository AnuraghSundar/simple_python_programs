__author__ = 'Code Hobbits'

"""
Write a function to check if a given string is palindrome or not

"""


def is_palindrome(s):
    # get length of the string
    l = len(s)

    # create a counter variable
    counter = 1

    # create a variable flag. flag=1 -> palindrome. flag=0 -> not palindrome
    flag = 1 # assume the string is palindrome

    # run a while loop from beginning of the string to the middle of the string
    while counter < l/2:
        # check is the nth character from front of the string equals
        # the nth character from back of the string
        if s[counter-1] != s[-(counter)]:
            # if the characters don't match, string is not a palindrome
            flag = 0
            # break out of the loop. no need to check further
            break
        # increment counter
        counter += 1
    # return flag
    return flag


print("Enter a string:")
iString = input()
result = is_palindrome(iString)
print(result)


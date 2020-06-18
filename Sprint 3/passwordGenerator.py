import random

'''    
string.ascii_letters
    The lowercase and uppercase letters 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

string.punctuation
    String of ASCII characters which are considered punctuation characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

string.digits
    The string '0123456789'
'''
from string import (ascii_letters, digits, punctuation)


'''
characters : str
    A string containing password character set.
'''
characters = ''.join([ascii_letters, digits, punctuation])

'''
Return a string of n-length from the character set above.
'''
def generateNewPassword(n = 12):
    return ''.join(random.sample(characters, k = n))

if __name__ == "__main__":
    print(generateNewPassword())

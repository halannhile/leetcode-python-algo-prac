"""
https://leetcode.com/problems/palindrome-number
"""

# the best method to solve this without converting the integer into string:

# Iterative function to check if given number is a palindrome or not
def isPalindrome(num):

    # n stores the given integer
    n = num


    # rev stores the reverse of the given integer
    rev = 0

    while n:
        # this will store last digit of n in variable r
        # eg. if n is 1234, then r would be 4
        r = n % 10

        # add r in one's place in rev
        # eg. if rev = 65 and r = 4, then rev = 654
        rev = rev * 10 + r

        # remove last digit from n
        # eg. if n is 1234, then the n would be 123
        n = n // 10

    # this expression will return 1 if given number is equal to
    # its reverse else it will return 0
    return num == rev


# test:

if __name__ == '__main__':

	n = 12321

	if isPalindrome(n): print(True)
	else: print(False)




##############################################################################################

# this is how i did it, which is way too long and involves converting the integer into string
# there sure are better ways to go about it that i am not skilled enough to think of

def isPalindrome(x):
    # :type x: int
    # :rtype: bool

    string = str(x)

    # -121 in reverse will be 121-. hence, return false for negative numbers
    if x < 0:
        return False

    # 1 in reverse is 1. hence, return true for one-digit numbers
    elif len(string) == 1:
        return True

    # positive numbers: 
    elif x > 0:

        # positive numbers with length being an even number and higher than 2, e.g. 1221
        if len(string) % 2 == 0 and len(string) > 2:

            # e.g. if [1,2] == [2,1][::-1] then return true. recall that [::-1] is to reverse list. 
            # can also use list.reverse() but sometimes this doesn't work
            a = int(len(string)/2)
            if string[:a] == string[a:][::-1]:
                return True
            else:
                return False

            # positive numbers with length being 2, e.g. 99, 78
        elif len(string) == 2:

            # e.g. 99
            if string[0] == string[1]:
                return True

            # e.g. 78
            else:
                return False

        # positive numbers with length being an odd number, e.g. 12321 
        elif len(string) % 2 == 1:

            # convert from str(x) = "12321" into x = [1,2,3,2,1]
            list_digits = [int(i) for i in string]

            # all digits up until the middle digit, excluding the middle digit
            a = int(((len(list_digits) - 1) / 2))

            # all digits after the middle digit, excluding the middle digit: 
            b = int(((len(list_digits) + 1) / 2))

            # e.g. if [1,2] == [2,1][::-1] then return true
            if list_digits[:a] == list_digits[b:][::-1]:
                return True
            else:
                return False




# test:
var1 = 12321
print(isPalindrome(var1))

var2 = 1234
print(isPalindrome(var2))


"""
alternative approaches:  

def isPalindrome(self, x):
    return str(x) == str(x)[::-1]
    
    
or: 

def isPalindrome(self, x: int) -> bool:
    x=str(x)
    if x[::-1]==x: return True
    
    
or: 

def isPalindrome(self, x: int) -> bool:
    polindrom=True
    if str(x)!=str(x)[::-1]: polindrom=False
    return polindrom
    
    
or: 
def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
        
        
        
or: 

def isPalindrome(self, x):
    revx = (str(x)[::-1])
    return revx == str(x)
    


or: 
return False if x < 0 else x == int(str(x)[::-1])




or: 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #O(N) time complexity where N is the number of elements in S
        # O(1) space
        L, R = 0, len(s) - 1
        
        while L < R:
            if not s[L].isalnum():
                L += 1
            elif not s[R].isalnum():
                R -= 1
            else:
                if s[L].upper() != s[R].upper():
                    return False
                L += 1
                R -= 1
        return True

# can also do it so that you simply join the letters together (condition where it isalnum) and then just check whether it is equal to its reverse
# This is faster but takes up more space
def validpalindrome(s):
        s = ''.join(ch.lower() for ch in s if ch.isalpha() or ch.isdigit())
        return s == s[::-1]
        #space: O(N)
"""




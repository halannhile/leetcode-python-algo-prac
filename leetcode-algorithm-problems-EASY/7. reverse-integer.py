"""
https://leetcode.com/problems/reverse-integer/
"""



def reverse(x):

    # :type x: int
    # :rtype: int

    # return 0 if integer falls outside the 32-bit signed integer range: [−2**31,  2**31 − 1]
    if x >= 2 ** 31 - 1 or x <= -2 ** 31:
        return 0

    else:
        string = str(x)

        if x >= 0:  # positive numbers
            res = string[::-1]  # reverse ordering of all digits

        else:  # negative numbers
            digits = string[1:]  # extract digits part of string, i.e. without the - sign
            reversed_digits = digits[::-1]
            res = "-" + reversed_digits  # making it negative

        # return 0 if integer falls ourside 32-bit signed integer range: [−2**31,  2**31 − 1]
        if int(res) >= 2 ** 31 - 1 or int(res) <= -2 ** 31:
            return 0

        else:
            return int(res)


"""
# alternative approach: 

class Solution:
    def reverse(x):

        s = str(abs(x))

        reversed = int(s[::-1])

        if reversed > 2147483647:
            return 0

        return reversed if x > 0 else (reversed * -1)
"""


# test:

x = -123
print(reverse(x))

y = -2894728
print(reverse(y))


# additional resource:
# https://www.youtube.com/watch?v=XpvNcex-rc0&feature=youtu.be
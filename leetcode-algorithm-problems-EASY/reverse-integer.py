"""
https://leetcode.com/problems/reverse-integer/
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    # return 0 if integers fall outside the 32-bit signed integer range: [−2**31,  2**31 − 1]
    if x > 2 ** 31 - 1 or x < -2 ** 31:
        return 0
    else:
        if x >= 0:
            res = str(x)[::-1]  # reverse ordering of all digits
        else:
            # making string positive, then reverse ordering of digits, then make it negative
            res = -1 * int(str(x*-1)[::-1])

            # alternative method:

            # digits = string[1:] # extract digits part of string, i.e. without the - sign
            # reversed_digits = digits[::-1]
            # res = - reversed_digits # making it negative

    return res

# test:

x = -123
print(reverse(x))

y = -2894728
print(reverse(y))


# additional resource:
# https://www.youtube.com/watch?v=XpvNcex-rc0&feature=youtu.be
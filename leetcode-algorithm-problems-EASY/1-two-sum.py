"""
https://leetcode.com/problems/two-sum/
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    h = {} # dictionary: https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python#:~:text=About%20Dictionaries%20in%20Python,with%20commas%20%2C%20between%20each%20pair.&text=As%20with%20lists%20we%20can,printing%20the%20reference%20to%20it.,
           # https://discuss.codecademy.com/t/i-dont-get-what-is-the-difference-between-and-in-python/46479
    for i, num in enumerate(nums): # on enumerate(): https://book.pythontips.com/en/latest/enumerate.html
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]


"""
alternative approach #1: 

def twoSum(self, nums, target):
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i
"""



"""
alternative approach #2: 

def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []
"""



"""
alternative approach 3: 

def twoSum(nums, target):
    num_set = {}
    for num_index, num in enumerate(nums):
        if (target - num) in num_set:
            return [num_set[target - num], num_index]
        num_set[num] = num_index
"""



"""
alternative approach 4: 

def twoSum(self, nums, target):
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i
"""


# testing:

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))
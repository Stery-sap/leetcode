class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_values = {}
        for i,num in enumerate(nums):
            element = target - num
            if element in num_values:
                return[num_values[element],i]
            num_values[num] = i
        return []

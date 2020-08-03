"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution(object):

    # 暴力解法，时间复杂度n平方，空间复杂度1
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i, j]
        raise Exception('no two sum solution')

    # def twoSum(self, nums, target):
        # pass


s = Solution()
# print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([2, 7, 11, 15], 18))

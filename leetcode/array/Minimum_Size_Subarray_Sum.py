import sys

"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，
并返回其长度。如果不存在符合条件的连续子数组，返回 0。

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的连续子数组。
"""


class Solution(object):
    # 暴力解法
    # def minSubArrayLen(self, s, nums):
    #     if len(nums) == 0:
    #         return 0

    #     min_len = sys.maxsize
    #     for i in range(len(nums)):
    #         sum = 0
    #         for j in range(i, len(nums)):
    #             sum += nums[j]
    #             if sum >= s:
    #                 length = j - i + 1
    #                 if length < min_len:
    #                     min_len = length

    #     if min_len != sys.maxsize:
    #         return min_len
    #     else:
    #         return 0

    """双指针+滑动窗口法，不同于暴力解法，本质上只把数组遍历了一遍，所以是O(N)的复杂度"""
    def minSubArrayLen(self, s, nums):
        min_len = sys.maxsize
        l = 0
        tmp = 0
        for r in range(len(nums)):
            tmp += nums[r]
            while tmp >= s:
                min_len = min(min_len, r-l+1)
                tmp -= nums[l]
                l += 1

        return min_len if min_len != sys.maxsize else 0

if __name__ == "__main__":
    s = Solution()
    nums = [2,3,1,2,4,3]
    target = 0
    res = s.minSubArrayLen(target, nums)
    print(res)
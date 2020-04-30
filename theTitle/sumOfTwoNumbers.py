#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for y in range(i+1, len(nums)):
                if nums[i] + nums[y] == target:
                    return [i, y]
        return None


class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, value in enumerate(nums):
            diff = target - value
            if diff in nums and nums.index(diff) != index:
                return [index, nums.index(diff)]
        return None


class Solution2:

    def twoSum(self, nums, target):
        """
        :param nums: is List[int]
        :param target: is int
        :return: is List[int]
        """
        results = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in results:
                return [results[difference], index]
            else:
                results[value] = index
        return None

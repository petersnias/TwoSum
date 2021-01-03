'''
TwoSum

Descriptions:  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Author:  Peters, Nia S.

Date Started: 2 Jan 2020

Last Updated:  2 Jan 2020


'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for ele1 in nums:
            for ele2 in nums:
                if(target - ele1 == ele2):
                    output = [ele1,ele2]
                    break;
                else:
                    output = "No Solution Found!"

        return output



a = Solution()

out = a.twoSum([6,2,3,5,2,7,1],6)

print(out)

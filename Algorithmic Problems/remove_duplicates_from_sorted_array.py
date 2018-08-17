class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        currNum = nums[0]
        count = 1
        while count < len(nums):
            if currNum == nums[count]:
                del nums[count]
                count -= 1
            else:
                currNum = nums[count]
            count += 1
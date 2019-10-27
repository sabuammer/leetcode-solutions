class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        while low <= high:
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                    mid = (low + high) // 2
                else:
                    low = mid + 1
                    mid = (low + high) // 2
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                    mid = (low + high) // 2
                else:
                    high = mid - 1
                    mid = (low + high) // 2

        return -1

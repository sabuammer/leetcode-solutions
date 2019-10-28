class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums[0], nums[1])
        elif nums[0] < nums[-1]:
            return nums[0]  # Array is still sorted in increasing order

        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        while True:
            if high == low:
                # Could also do nums[high], since they'd be equal here
                return nums[low]
            elif high - low == 1:
                return min(nums[low], nums[high])
            elif nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return nums[mid+1]
            elif nums[mid] > nums[low]:
                low = mid + 1
                mid = (low + high) // 2
            elif nums[mid] < nums[low]:
                high = mid - 1
                mid = (low + high) // 2

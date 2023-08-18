class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target:
            ret_idx = len(nums)
            if target <= nums[0]:
                ret_idx = 0
        else:
            ret_idx = 0

        for i in range(1, len(nums)):
            if nums[i - 1] < target and target <= nums[i]:
                ret_idx = i
                break

        return ret_idx
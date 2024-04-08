class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
    #    cur = 0 
        preleft = 0
        for i in range(len(nums)):
            preright = total - preleft - nums[i]
            if preright == preleft:
                return i
            preleft += nums[i]

        return -1

        
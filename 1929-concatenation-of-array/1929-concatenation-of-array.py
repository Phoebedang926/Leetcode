class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = nums
        nums.extend(nums)
        # for i in nums:
        #     nums.append(i)
        return nums
        
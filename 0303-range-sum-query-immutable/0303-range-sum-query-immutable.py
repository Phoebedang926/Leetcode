class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for num in nums:
            cur += num
            self.prefix.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        preright = self.prefix[right]
        preleft = self.prefix[left - 1] if left > 0 else 0
        return (preright - preleft)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
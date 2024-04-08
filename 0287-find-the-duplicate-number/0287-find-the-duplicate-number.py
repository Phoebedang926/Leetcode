class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        slow2 = 0
        while True:
            if slow == slow2:
                return slow
            slow = nums[slow]
            slow2 = nums[slow2]


        

        
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        stored_nums = set()
        for number in nums:
            if number in stored_nums:
                return True
            stored_nums.add(number)     
        return False
        
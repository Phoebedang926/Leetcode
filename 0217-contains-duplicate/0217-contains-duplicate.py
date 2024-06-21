class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                return True
            if n not in hashmap:
                hashmap[n] = 1
        return False

        
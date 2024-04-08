class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = {0: 1}
        cursum = 0
        count = 0
        for n in nums:
            cursum += n
            diff = cursum - k
            count += prefixsum.get(diff,0)
            prefixsum[cursum] = 1 + prefixsum.get(cursum,0)
        return count

        


        
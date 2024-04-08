class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        prevsum = {0:1}


        for i in range(len(nums)):
            currsum = {}
            for s, count in prevsum.items():
                currsum[s + nums[i]] = currsum.get(s+nums[i], 0) + count
                currsum[s - nums[i]] = currsum.get(s-nums[i], 0) + count
            prevsum = currsum

        return prevsum.get(target,0) 
                


        # prevsum = [0]


        # for i in range(len(nums)):
        #     currsum = []
        #     for s in prevsum:
        #         currsum.append(s + nums[i])
        #         currsum.append(s - nums[i])
        #     prevsum = currsum

        # return prevsum.count(target) 
                

        
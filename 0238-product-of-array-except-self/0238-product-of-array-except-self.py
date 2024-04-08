class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        pre = 1
        for i in range(length):
            res[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(length-1,-1,-1):
            res[i] = res[i]*post
            post *= nums[i]      
        return res



        # output = [1] * len(nums)
        # range_nums = list(range(len(nums)))
        # prefix = 1
        # for i in range_nums:
        #     output[i] = prefix
        #     prefix *= nums[i]

        # postfix = 1
        # for x in range_nums[::-1]:
        #     output[x] *= postfix
        #     postfix *= nums[x]
        # return output


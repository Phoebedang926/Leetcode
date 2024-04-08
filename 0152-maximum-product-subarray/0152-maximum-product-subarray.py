class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        minProd = 1
        maxProd = 1
        for i in nums:
            if i == 0:
                minProd, maxProd = 1, 1
            tempmax = i * maxProd
            maxProd = max(i * maxProd,i * minProd, i)
            minProd = min(tempmax, minProd * i, i)
            
            result = max(result, maxProd)

        return result

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         currentProd1 = nums[0]
#         maxProd1 = nums[0]
#         for i in nums[1:]:
#             if currentProd1 == 0:
#                 currentProd1 = 1
#             currentProd1 *= i
#             maxProd1 = max(maxProd1, currentProd1)

#         currentProd2 = nums[-1]
#         maxProd2 = nums[-1]
#         for i in nums[:-1][::-1]:
#             if currentProd2 == 0:
#                 currentProd2 = 1
#             currentProd2 *= i
#             maxProd2 = max(maxProd2, currentProd2)

#         maxProd = max(maxProd1, maxProd2)
#         return maxProd


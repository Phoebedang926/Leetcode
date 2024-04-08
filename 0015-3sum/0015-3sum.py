class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num0 in enumerate(nums):
            if i > 0 and num0 == nums[i-1]:
                continue
            
            l,r= i+1, len(nums)-1
            while l<r:
                threesum = num0 + nums[l] + nums[r]
                if threesum ==0:
                    res.append([num0, nums[l], nums[r]])
                    l +=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif threesum <0:
                    l +=1
                else: 
                    r -=1
        
        return res
                









# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         prevMap = []
#         temp_result = []
        
#         for i in range(len(nums)-1):
#             lookup_value = 0 - nums[i] - nums[i+1]
#             if lookup_value in prevMap:
#                 temp_result.append([nums[i], nums[i+1], lookup_value])

#             else:
#                 prevMap.append(nums[i])


#         unique_list = list(set(tuple(inner_list) for inner_list in temp_result))

#         result_list = [list(inner_tuple) for inner_tuple in unique_list]


#         return result_list

#         # return temp_result
            

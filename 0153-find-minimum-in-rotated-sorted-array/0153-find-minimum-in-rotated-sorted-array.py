
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0 , len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l+r)//2
            res = min(res,nums[m])
            if nums[m] >= nums[r]:
                l = m+1
            else:
                r = m-1
        return res

            

            





# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         result = min(nums)
#         return result


# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         if nums[0]<nums[-1]:
#             result= nums[0]
#         else:
#             split_point = len(nums)/2
#             first_part = nums[:split_point]
#             second_part = nums[split_point:]
#             if first_part[-1]>second_part[0]:
#                 result = first_part[-1]
#             else


# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         split_point = len(nums)//2
#         left_point = 0
#         right_point = len(nums)-1
#         while left_point <= right_point:
#             if nums[split_point] < nums[right_point]:
#                 result = nums[left_point]
#                 break
#             elif nums[split_point] > nums[split_point+1]:
#                 result = nums[split_point+1]
#                 break
#             left_point = split_point + 1
#             split_point = (left_point + right_point)//2 
            
 
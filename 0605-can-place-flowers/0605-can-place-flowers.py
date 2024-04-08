# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         if n ==0:
#             return True
#         for i in range(len(flowerbed)):

#             if flowerbed[i] == 0 and (
#                 len(flowerbed) == 1 or
#                 (len(flowerbed)> 1 and i == 0 and flowerbed[i+1] ==0) or 
#                 ( 0 < i < (len(flowerbed) -1) and flowerbed[i-1]  == 0 and flowerbed[i+1] ==0) 
#                 or (i == len(flowerbed) -1 and flowerbed[i-1] ==0) ):
#                 flowerbed[i] = 1
#                 n -=1
#                 if n ==0:
#                     return True
#         return False
            

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        i=0
        while i < len(flowerbed):
            if (i==0 or flowerbed[i-1]==0)and (flowerbed[i]==0)and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                n=n-1
                i=i+2
                if n == 0:
                    return True
            else:
                i=i+1
        return False

            
            
            

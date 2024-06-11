class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=[0,0,0]
        for c in nums:
            count[c] +=1
            
        inums = 0
        for i,c in enumerate(count):
            for n in range(c):
                nums[inums] = i
                inums +=1
        
            
        
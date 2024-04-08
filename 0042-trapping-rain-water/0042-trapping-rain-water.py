class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxl = height[0]
        maxr = height[-1]
        trapwater = 0
        while l < r:
            if maxl <= maxr:
                l +=1
                maxl = max(maxl, height[l])
                trapwater += maxl - height[l]
            else:
                r -=1
                maxr = max(maxr, height[r])
                trapwater += maxr - height[r]


        return trapwater
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        maxcandies = max(candies)
        for i in candies:
            if i + extraCandies >= maxcandies:
                res.append(True)
            else:
                res.append(False)
        return res




# candies[i] + extraCandies <= max(candies)
# max - extracan
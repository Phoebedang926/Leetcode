class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0  
        currsum = sum(arr[:k-1])

        for l in range(len(arr)-k+1):
            r = l+k-1
            currsum += arr[r]
            if (currsum/k) >= threshold:
                res += 1
            currsum -= arr[l]
        return res




        # l = 0
        # for r in range(k-1, len(arr)):
        #     currsum += arr[r]
        #     if r-l+1 > k:
        #         currsum -= arr[l]
        #         l += 1

        #     avg = currsum/ k
        #     if avg >= threshold:
        #         res += 1

        # return res
            

        
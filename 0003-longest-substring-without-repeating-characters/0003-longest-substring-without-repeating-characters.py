class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        length, l = 0, 0
        for r in range(len(s)):
            while s[r] in substring:                
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            length = max(length, r-l+1)
        return length



        



        # # res = ""
        # lenstr = 0
        # for i in range(len(s)):
        #     l, r = i, i
        #     while r < len(s) and s[r] not in s[l:r]:
        #         if (r-l+1) > lenstr:
        #             # res = s[l:r+1]
        #             lenstr = r-l+1
        #         r +=1
        # return lenstr

        
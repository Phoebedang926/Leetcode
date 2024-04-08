class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = "aeiouAEIOU"
        s = list(s)
        left, right = 0, len(s)-1
        while left < right:
            if s[left] in vowel and s[right] in vowel:
                # tpleft = s[left]
                # tpright = s[right]
                # s[left] = tpright
                # s[right] = tpleft
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] in vowel and s[right] not in vowel:
                right -= 1
            elif s[left] not in vowel and s[right] in vowel:
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(s)                




            

        
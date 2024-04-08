class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        import re
        s = re.sub(r'[^a-z0-9]', '', s)
        return s == s[::-1]

        # reverses = list(s)[::-1]
        # reverses1 = ''.join(reverses)
        # return s == reverses1

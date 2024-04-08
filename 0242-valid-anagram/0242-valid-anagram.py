class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorteds = ''.join(sorted(s))
        sortedt = ''.join(sorted(t))
        if sorteds == sortedt:
            return True
        else:
            return False
        
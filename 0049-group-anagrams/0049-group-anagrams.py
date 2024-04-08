class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ana = {}
        for i in strs:
            sortedi = ''.join(sorted(i))
            if sortedi in ana:
                ana[sortedi].append(i)
            else:
                ana[sortedi] = [i]
        return ana.values()

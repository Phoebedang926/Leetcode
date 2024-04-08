class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        result = ""
 
        minlen = min(len(word1), len(word2))
        while p1 < minlen and p2 < minlen:
            result += word1[p1] + word2[p1]
            p1 +=1 
            p2 +=1
        # if len(word1) > len(word2):
        #     result += word1[minlen:]
        # elif len(word1) < len(word2):
        #     result += word2[minlen:]
        # else:
        #     return result
        result += word1[minlen:] + word2[minlen:]
        return result




        
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lenw1, lenw2 = len(word1), len(word2)
        cache = [[float('inf')]*(lenw2+1) for i in range(lenw1+1)]
        for i in range(lenw1+1):
            cache[i][lenw2] = lenw1 -i
        for j in range(lenw2+1):
            cache[lenw1][j] = lenw2 - j     

        for i in range(lenw1 - 1, -1, -1):
            for j in range(lenw2 - 1, -1, -1):
                if word1[i] == word2[j]:                    
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])
        
        return cache[0][0]
class Solution:
    def minimumPushes(self, word: str) -> int:
        m = Counter(word)
        v = sorted(m.values(), reverse=True)
        ans = 0
        for i in range(0,len(v)):
            ans+=v[i]*((i//8)+1)
        return ans


        # result = 0
        # f = collections.Counter(word)
        # for i, w in enumerate(sorted(f.values(),reverse=True)):
        #     result += ((i//8)+1) * w
        
        # return result

        
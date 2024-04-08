class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1 + str2 != str2 + str1:
            return ""
        else:
            if len(str1) == len(str2):
                return str1
            else:
                len1 = len(str1)
                len2 = len(str2)
                def isdivisor(l):
                    if len1 % l or len2 % l:
                        return False
                    f1 = len1 // l
                    f2 = len2 // l     
                    return str1[:l] * f1 == str1 and str2[:l] *f2 ==str2                   

                for l in range(max(len1,len2) - min(len1,len2), 0, -1):
                    if isdivisor(l):
                        return str1[:l]





        # if len(str1) == len(str2):
        #     if str1 != str2:
        #         return ""
        #     else: 
        #         return str1


        # minlen = min(len(str1), len(str2))
        # result = str1[minlen:] + str2[minlen:]
        # rep1 = len(str1) // len(result)
        # rep2 = len(str2) // len(result)
        # if result * rep1 == str1 and result * rep2 == str2:
        #     return result
        # else:
        #     return ""






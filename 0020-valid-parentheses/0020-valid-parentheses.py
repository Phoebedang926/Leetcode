class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = { ")" : "(" , "]" : "[", "}" : "{" }
        for i in s:
            if i in hashmap:
                if stack and hashmap[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack 
        # if len(s) % 2:
        #     return False
        # stack = []
        # for i in s:
        #     if i in "({[":
        #         stack.append(i)
        #     else:
            
        #         if i == ']' and stack and '[' == stack[-1] :
        #             stack.pop() 
        #         elif i == ')' and stack and '(' == stack[-1]:
        #             stack.pop()    
        #         elif i == '}' and stack and '{' == stack[-1]:
        #             stack.pop()  
        #         else:
        #             return False
        # return not stack 

                                
                
            

            

        
        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ")":"(",
            "}": "{",
            "]":"["
        }
        for i in s:
            if i in '{([':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if map[i] != stack.pop():
                    return False
        return len(stack) == 0 

                
            

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        if len(s) == 0:
            return True 
        par_dict = {"{":"}", "(":")", "[":"]" }
        par_stack = []
        for p in s:
        # Check if open and then push
            if p in par_dict: 
                par_stack.append(p)
            elif p in par_dict.values(): # one of the three valid closers 
                if len(par_stack) > 0 and par_dict[par_stack[-1]] == p:
                    par_stack.pop()
                else:
                    return False # doesnt match no need to evaluate further
        return True if len(par_stack) == 0 else False 
        
        
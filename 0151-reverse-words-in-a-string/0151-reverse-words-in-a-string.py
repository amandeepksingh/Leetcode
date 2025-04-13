class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words = [c for c in words if c != " "]
        print(words)
        p1 = 0 
        p2 = len(words) -1 
        to_ret = ""
        while p1 <= p2:
            temp = words[p1]
            words[p1] = words[p2]
            words[p2] = temp
            p1 = p1 + 1
            p2 = p2 - 1
        return " ".join(c for c in words if c != "")
            

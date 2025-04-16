class Solution:
    def removeStars(self, s: str) -> str:
        wstack = []
        for i in s:
            if i != "*":
                wstack.append(i)
            else:
                wstack.pop()
        return "".join(wstack)
        
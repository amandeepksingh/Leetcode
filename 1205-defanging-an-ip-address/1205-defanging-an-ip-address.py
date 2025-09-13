class Solution:
    def defangIPaddr(self, address: str) -> str:
        l = address.split(".")
        r = ""
        for n in range(len(l)-1):
            r = r + l[n] + "[.]"
        return r + l[-1]

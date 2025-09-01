from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys or not self.keys[key]:
            return ""
        
        ts = self.keys[key]
        
        if timestamp < ts[0][0]:  # before first set
            return ""
        
        # Binary search for largest timestamp <= target
        l, r = 0, len(ts) - 1
        res = ""
        
        while l <= r:
            m = (l + r) // 2
            if ts[m][0] == timestamp:
                return ts[m][1]  # exact match
            elif ts[m][0] < timestamp:
                res = ts[m][1]  # candidate
                l = m + 1
            else:  # ts[m][0] > timestamp
                r = m - 1
                
        return res


        # if before set (ie before min timestamp) - return ""
        # so if we have timestamps for setting 3, 5, 9 --> before 3 - "", 3-5 pw1, 5-9 pw2 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
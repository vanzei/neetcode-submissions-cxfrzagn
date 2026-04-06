class TimeMap:

    def __init__(self):
        self.hash = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash:
            self.hash[key].append([value, timestamp])
        else:
            self.hash[key] = [[value, timestamp]]


    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.hash.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = l + (r - l) // 2
            print(values, m)
            print(values[m][1])
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
                
        

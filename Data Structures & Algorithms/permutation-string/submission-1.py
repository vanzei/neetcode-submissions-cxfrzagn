class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        counter_s1 = Counter(s1)
        i = 0
        j = i + l1

        while j <= len(s2):
            counter_s2 = Counter(s2[i:j])
            if counter_s1 == counter_s2:
                return True
            i += 1
            j += 1
        return False

        

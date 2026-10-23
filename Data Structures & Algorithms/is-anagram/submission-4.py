class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        counts = {}
        countt = {}

        for i in s:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 0
        
        for j in t:
            if j in countt:
                countt[j] += 1
            else:
                countt[j] = 0
        
        return counts==countt
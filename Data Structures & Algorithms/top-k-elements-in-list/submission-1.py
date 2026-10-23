class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        result = []
        for i in nums:
            if i in d:
                d[i] += 1
            
            else:
                d[i] = 1
        
        d = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))

        for key, value in d.items():
            result.append(key)
        
        
        return result[:k]
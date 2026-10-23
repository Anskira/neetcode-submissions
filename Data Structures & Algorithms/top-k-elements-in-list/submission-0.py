class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        d = sorted(d.items(), key=lambda item: item[1], reverse = True)
        # d1 = {i[0]: i[1] for i in d}
        result = []

        for i in range(k):
            result.append(d[i][0])
        # for key, v in d1.items
        return result
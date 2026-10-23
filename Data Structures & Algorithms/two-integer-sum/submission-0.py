class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}
        result = []
        for i, v in enumerate(nums):

            if v in d:
                result.append(d[v])
                result.append(i)

            else:
                d[v]=i
                d[target-v]=i
            print(i, v)
        
        return result

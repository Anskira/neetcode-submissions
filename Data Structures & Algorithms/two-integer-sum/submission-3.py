class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l1 = []
        result = []
        for i, v in enumerate(nums):
            l1.append(v)
            temp = target - v
            if temp in l1 and i!=l1.index(temp):
                result.append(min(i, l1.index(temp)))
                result.append(max(i, l1.index(temp)))
        return result

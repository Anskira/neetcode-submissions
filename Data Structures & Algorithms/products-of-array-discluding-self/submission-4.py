class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zeros = 0
        f = False
        f1 = False

        for n in nums:
                         
            if n==0:
                zeros+=1
                f = True
            
            else:
                f1 = True
                p*=n
        if zeros>1:
            return [0]*len(nums)   
        result = []
        if f1==False:
            return [0]*len(nums)
        for n in nums:
            if f:
                if n!=0:
                    result.append(0)
                else:
                    result.append(p)
            
            else:
                result.append(p//n)

        return result

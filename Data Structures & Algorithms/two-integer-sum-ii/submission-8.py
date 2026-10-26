class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        result = []

        for i in range(len(numbers)-1):
            temp = target - numbers[i]
            
            s = i + 1
            e = len(numbers) - 1

            while s<=e:
                mid = (s + e) // 2

                if numbers[mid]<temp:
                    s = mid + 1
                
                elif numbers[mid]> temp:
                    e = mid - 1
                
                else:
                    return [i + 1, mid + 1]
            
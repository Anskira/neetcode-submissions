class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0

        count = 0
        uniq = {}
        while r<len(s):
            if s[r] in uniq:
                del uniq[s[l]]
                l+=1

            else:
                uniq[s[r]] =1 
                r+=1
            
            count = max(count, len(uniq))
        
        return count
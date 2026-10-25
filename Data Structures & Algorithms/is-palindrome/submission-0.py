class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        l = []
        for i in s:
            if i.isalnum():
                l.append(i.lower())
        
        l1 = l[::-1]
        # print(''.join(l1))

        if ''.join(l1)==''.join(l):
            return True
        
        return False
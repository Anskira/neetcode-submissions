class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        s_d = {}

        for i in s:
            if i in s_d:
                s_d[i]+=1
            else:
                s_d[i]=1

        for j in t:
            if j in s_d:
                s_d[j]-=1
            
            else:
                s_d[j]=1
        
        for k, v in s_d.items():
            if v>0:
                return False

        return True
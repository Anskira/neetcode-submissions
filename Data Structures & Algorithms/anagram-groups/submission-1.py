class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        # print(arr)

        for s in strs:
            arr = [0 for i in range(26)]
            for i in range(len(s)):
                arr[ord(s[i])-ord('a')] += 1
            
            t_arr = tuple(arr)
            if t_arr in d:
                d[t_arr].append(s)
            
            else:
                d[t_arr] = [s]
        
        # print(ord('b'))
        # print(d)

        result = []
        for k, v in d.items():
            result.append(v)
        return result
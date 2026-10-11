class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1={}
        hash2={}
        for num in s:
            if num in hash1:
                hash1[num]+=1
            else:
                hash1[num]=1
        for num in t:
            if num in hash2:
                hash2[num]+=1
            else:
                hash2[num]=1
        return hash1==hash2
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for num in strs:
            key=''.join (sorted(num))
            if key not in groups:
                groups[key]=[]
            groups[key].append(num) 
        return list(groups.values())
        
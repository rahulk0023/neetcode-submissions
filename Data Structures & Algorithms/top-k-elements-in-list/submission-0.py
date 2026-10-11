class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
     freq=Counter(nums) 
     ans=[]
     while k>0:
        num=max(freq,key=freq.get)
        ans.append(num)
        del freq[num]
        k-=1
     return ans  
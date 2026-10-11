class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums))!=len(nums)
        hash={}
        for num in nums:
            if num in hash:
                return True
            else:
                hash[num]=1
        return False
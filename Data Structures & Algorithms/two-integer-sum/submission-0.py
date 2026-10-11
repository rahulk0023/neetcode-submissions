class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for num in range(len(nums)):
            compliment=target-nums[num]
            if compliment in hash:
                return [hash[compliment],num]
            else:
                hash[nums[num]]=num
        return [-1,-1]
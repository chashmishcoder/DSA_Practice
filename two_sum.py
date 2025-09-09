class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict((num, idx)for idx, num in enumerate(nums))
        
        for i in range(len(nums)):
            desired = target-nums[i]
            if desired in hash and hash[desired] != i:
                    return i, hash[desired]
            
        
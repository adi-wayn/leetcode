class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        s_nums = sorted(nums)

        for i in range(1, len(s_nums)):
            if s_nums[i] == s_nums[i - 1]:
                return True
        
        return False
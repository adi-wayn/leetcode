class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0

        prefixs = {0: 1}

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixs.get(diff, 0)
            prefixs[curSum] = 1 + prefixs.get(curSum, 0)
        
        return res
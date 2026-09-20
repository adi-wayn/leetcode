class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {} # val : index

        for i, n in enumerate(nums):
            rem = target - n
            if rem in prev_map:
                return [prev_map[rem], i]
            
            prev_map[n] = i
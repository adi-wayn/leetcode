class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        hashmap = {}

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)

        for _, v in hashmap.items():
            if v > 1:
                return True

        return False
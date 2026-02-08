class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)

        if n <= 1: return 0

        jumps = 0
        max_reach = 0
        last_jump_reach = 0

        for i in range(n-1):
            max_reach = max(max_reach, i+nums[i])

            if i == last_jump_reach:
                jumps += 1
                last_jump_reach = max_reach
                
        return jumps
    # Time Complexity: O(n)

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach: return False
            max_reach = max(max_reach, i+nums[i])

        return True
    # Time Complexity: O(n)

if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2,3,1,1,4])) # True
    print(s.canJump([3,2,1,0,4])) # False
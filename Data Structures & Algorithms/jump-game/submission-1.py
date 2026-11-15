from functools import cache


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        @cache
        def dfs(n):
            if n >= len(nums):
                return False

            if n == len(nums) - 1:
                return True
            
            for i in range(nums[n]):
                if dfs(n + i + 1) == True:
                    return True
        
        if dfs(0):
            return True

        return False

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in pMap:
                return [pMap[diff], i]

            pMap[n] = i

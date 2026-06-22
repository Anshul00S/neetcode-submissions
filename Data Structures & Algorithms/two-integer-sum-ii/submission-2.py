class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) -1

        while l < r:
            sol = numbers[l] + numbers[r]
            
            if sol == target:
                return [l + 1,r + 1]

            if sol > target:
                r -= 1
            
            if sol < target:
                l += 1

        
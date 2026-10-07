class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for index, x in enumerate(nums):
            ans = target - x
            if ans in seen:
                return [seen[ans], index]
            seen[x] = index

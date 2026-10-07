class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}
        for index, x in enumerate(nums):
            if x in seen:
                return True
            seen[x] = index
        return False
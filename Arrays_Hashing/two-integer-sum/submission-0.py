class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int] | None:
        # Time: O(n), Space: O(n)
        # Hash map of value -> index seen so far.
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return None
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxs = 0

        while left < right:
            w = right - left
            h = min (heights[left], heights[right])
            s = w * h
            maxs = max(s, maxs)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxs

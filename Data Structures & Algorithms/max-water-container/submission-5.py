class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxs = 0

        while left < right:
            w = right -left
            h = min(height[left], height[right])
            s = w*h
            maxs = max(s, maxs)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxs


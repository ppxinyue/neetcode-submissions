class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        stack = []

        for i in range(n):
            while stack and height[i]>height[stack[-1]]:
                bottom = height[stack.pop()]
                if stack:
                    r = height[i]
                    l = height[stack[-1]]
                    h = min(r, l) - bottom
                    w = i - stack[-1] -1

                    res += h * w

            stack.append(i)
        
        return res
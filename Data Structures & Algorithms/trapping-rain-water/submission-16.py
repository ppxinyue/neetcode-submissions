class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()
            
                if not stack:
                    break
                                
                width = i - stack[-1] - 1
                high = min(height[i],height[stack[-1]])-height[bottom]
                water += width * high

            stack.append(i)

        return water
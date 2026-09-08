class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                bottom = stack.pop()
                
                if not stack:
                    break
                    
                left = stack[-1]
                right = i

                bounded_h = min(height[left],height[right]) - height[bottom]
                width = right - left -1

                water += bounded_h * width            
            
            stack.append(i)

        return water
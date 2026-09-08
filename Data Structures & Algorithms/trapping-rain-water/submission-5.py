class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax = rmax = 0
        water = 0


        while l < r:
            lmax = max(height[l], lmax)
            rmax = max(height[r], rmax)

            if lmax < rmax:
                water += lmax - height[l]
                l += 1
            else:
                water += min(lmax, rmax) - height[r]
                r -= 1
        
        return water
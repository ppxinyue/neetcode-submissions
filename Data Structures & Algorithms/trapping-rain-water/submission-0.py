class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = rmax = 0
        l = 0
        r = len(height) - 1
        s = 0

        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])

            if lmax < rmax:
                s += lmax - height[l]
                l += 1
            else:
                s += rmax - height[r]
                r -= 1
        return s



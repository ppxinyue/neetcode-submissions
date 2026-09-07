class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for i, c in enumerate(t):
            need[c] = 1 + need.get(c, 0)

        left = 0
        res_length = float('inf')
        res = [-99, -99]
        curr = {}
        have = 0
        need_count = len(need.keys())

        for right, c in enumerate(s):
            curr[c] = 1 + curr.get(c, 0)
            if c in need and curr[c] == need[c]:
                have += 1

            while left<=right and have == need_count:
                if right-left+1 <res_length:
                    res = [left, right]
                    res_length = right - left + 1
                
                leftc = s[left]
                curr[leftc] -= 1
                if leftc in need and curr[leftc] < need[leftc]:
                    have -= 1
                left += 1

        if res == [-99, -99]:
            return ""
        else:
            return s[res[0]: res[1]+1]

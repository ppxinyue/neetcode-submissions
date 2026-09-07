class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for i, c in enumerate(t):
            need[c] = 1 + need.get(c, 0)
        
        left = 0
        curr = {}
        window = ''
        shortest_window = ''
        have = 0
        need_count = len(need.keys())
        succ = 0


        for right, c in enumerate(s):
            curr[c] = 1 + curr.get(c, 0)

            if c in need and curr[c] == need[c]:
                have += 1
            
            while have == need_count:
                window = s[left:right+1]
                if succ == 0:
                    shortest_window = window
                    succ += 1
                
                if len(window) < len(shortest_window):
                    shortest_window = window
                
                curr[s[left]] -= 1
                if s[left] in need and curr[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
                

        return shortest_window
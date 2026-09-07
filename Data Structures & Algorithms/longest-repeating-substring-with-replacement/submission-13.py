class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        longest = 0
        max_freq = 0

        for right, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)
            max_freq = max(count.values())
            
            while left < right and (right-left+1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                max_freq = max(count.values())
            
            longest = max(longest, right - left + 1)

        return longest
                

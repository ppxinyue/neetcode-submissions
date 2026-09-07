class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        right = 0
        longest = 0
        max_freq = 0

        for right, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)
            max_freq = max(count.values())
            window_length = right - left + 1
            
            while left < right and window_length - max_freq > k:
                count[s[left]] = max(count.get(s[left], 0) - 1, 0)
                left += 1
                window_length = right - left + 1
                max_freq = max(count.values())
            

            print(left, right)
            longest = max(longest, right - left + 1)

        return longest
                

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        for i, num in enumerate(nums):
            target = -num
            seen = dict()
            
            for j in range(i+1, len(nums)):
                need = target - nums[j]

                if need in seen:
                    triplet = tuple(sorted([num,nums[j],need]))
                    res.add(triplet)

                seen[nums[j]]=j
        
        return [list(t) for t in res]
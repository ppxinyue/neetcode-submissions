class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i>0 and nums[i-1]== nums[i]:
                continue


            target = -num
            left = i + 1
            right = len(nums)-1

            while left < right:
                cur = nums[left] + nums[right]
                if cur < target:
                    left += 1
                elif cur > target:
                    right -= 1
                elif cur == target:
                    print(left,right)
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left<right and nums[left] == nums[left-1]:
                        left += 1

        return res
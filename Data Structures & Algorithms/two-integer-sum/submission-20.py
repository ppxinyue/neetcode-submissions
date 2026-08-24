class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = []
        for i, num in enumerate(nums):
            hashtable.append([num,i])
        
        hashtable.sort()
        i, j = 0, len(nums)-1
        while i<j:
            cur = hashtable[i][0] + hashtable[j][0]
            if cur == target:
                return [min(hashtable[i][1], hashtable[j][1]),max(hashtable[i][1], hashtable[j][1])]
            elif cur < target:
                i+=1
            else:
                j-=1
    

        
        
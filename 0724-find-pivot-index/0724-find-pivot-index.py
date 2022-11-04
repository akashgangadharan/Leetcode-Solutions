class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i = 0
        sum = 0
        while i < len(nums):
            sum = nums[i] + sum
            i+=1
        leftsum = 0
        for i,x in enumerate(nums):
            if leftsum == (sum - leftsum - x):
                return i
            leftsum += x
        return -1

            
        
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        array = []
        for i in range(len(nums)):
            if i == 0:
                array.append(nums[i])
                continue
            k = nums[i]
            t = array[i-1]
            array.append(k + t)
        return array
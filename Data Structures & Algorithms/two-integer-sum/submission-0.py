class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dc ={}
        ln = len(nums)
        for num in range(ln):
            left = target - nums[num]
            # x = -1
            if left in dc:
                return [dc[left],num]
            dc[nums[num]] = num;
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l1 = len(nums)
        unique_numbers = set(nums)
        l2 = len(unique_numbers)

        if(l1==l2):
            return False
        return True
        # l = len(nums)
        # for i in range (l):
        #     for j in range (i+1 , l) :
        #         if(nums[i]==nums[j]) :
        #             return True
        # return False
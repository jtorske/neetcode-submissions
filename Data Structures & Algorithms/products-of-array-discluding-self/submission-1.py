class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final=[]
        for i in range(len(nums)):
            quickproduct=1
            for j in range(len(nums)):
                if j != i:
                    quickproduct = quickproduct * nums[j]
            final.append(quickproduct)
        return final
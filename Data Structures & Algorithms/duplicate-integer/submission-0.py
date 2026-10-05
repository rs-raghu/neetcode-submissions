class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dt = {}
        for i in nums:
            if i not in dt:
                dt[i] = 1
            else:
                return True
        return False
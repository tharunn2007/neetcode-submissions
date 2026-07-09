class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        if len(numset)==len(nums):
            return False
        elif len(numset)<len(nums):
            return True
        else:
            pass

        
            


        
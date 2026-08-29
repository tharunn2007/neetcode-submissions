class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] !=9:
            digits[-1]+=1
            return digits
        if digits.count(9)==len(digits):
            for i in range(len(digits)):
                digits[i]=0
            digits.insert(0,1)
            return digits
        else:
            i=-1
            count9 = -1
            while digits[i]==9 and i>-len(digits):
                digits[i]=0
                count9-=1
                i-=1
            digits[count9]+=1
            return digits
                


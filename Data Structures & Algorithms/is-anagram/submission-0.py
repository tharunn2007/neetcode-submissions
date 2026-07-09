class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=s.strip()
        t=t.strip()
        listS=sorted(s)
        listT=sorted(t)
        if listT==listS:
            return True
        else: 
            return False



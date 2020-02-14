class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myDict = {}
        mySet = set()
        for i in range(0,len(s)):
            if s[i] not in myDict:
                if t[i] in mySet:
                    return False
                myDict[s[i]] = t[i]
                mySet.add(t[i])
            else:
                if myDict[s[i]] != t[i]:
                    return False
        return True
        
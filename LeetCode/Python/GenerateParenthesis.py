class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generateHelper(n, "", 0, 0, res)
        return res
    
    def generateHelper(self, n: int, s: str, left: int, right: int, resList: List[str]):
        if len(s) == n*2:
            resList.append(s)
        else:
            if left < n:
                self.generateHelper(n, s+"(", left+1, right, resList)
            if right < left:
                self.generateHelper(n, s+")", left, right+1, resList)
                
        
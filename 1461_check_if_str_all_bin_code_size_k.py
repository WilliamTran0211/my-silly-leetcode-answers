class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        seen = [False] * need
        
        mask = need - 1
        num = 0
        
        for i, ch in enumerate(s):
            num = ((num << 1) & mask) | int(ch)
            
            if i >= k - 1:
                if not seen[num]:
                    seen[num] = True
                    need -= 1
                    
                    if need == 0:
                        return True
                        
        return False

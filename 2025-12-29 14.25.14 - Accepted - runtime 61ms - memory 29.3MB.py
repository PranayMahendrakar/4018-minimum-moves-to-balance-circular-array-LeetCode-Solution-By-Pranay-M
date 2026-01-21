class Solution:
    def minMoves(self, balance: List[int]) -> int:
        if sum(balance) < 0:
            return -1
        
        # Find the negative index (at most 1)
        idx = -1
        for i, num in enumerate(balance):
            if num < 0:
                idx = i
                break
        
        if idx == -1:
            return 0  # All non-negative
        
        n = len(balance)
        
        # Two pointers expanding from the negative position
        left, right = (idx - 1 + n) % n, (idx + 1) % n
        ld, rd = 1, 1  # distances from idx
        
        sumx = -balance[idx]  # Amount needed
        cost = 0
        
        while sumx > 0:
            if ld < rd:
                wanted = min(balance[left], sumx)
                sumx -= wanted
                cost += wanted * ld
                left = (left - 1 + n) % n
                ld += 1
            elif ld > rd:
                wanted = min(balance[right], sumx)
                sumx -= wanted
                cost += wanted * rd
                right = (right + 1) % n
                rd += 1
            else:
                if balance[left] >= balance[right]:
                    wanted = min(balance[left], sumx)
                    sumx -= wanted
                    cost += wanted * ld
                    left = (left - 1 + n) % n
                    ld += 1
                else:
                    wanted = min(balance[right], sumx)
                    sumx -= wanted
                    cost += wanted * rd
                    right = (right + 1) % n
                    rd += 1
        
        return cost
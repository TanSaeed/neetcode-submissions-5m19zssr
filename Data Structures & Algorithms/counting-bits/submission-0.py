class Solution:
    def countBits(self, n: int) -> List[int]:
        
        answer = [0] * (n+1)

        for i in range(1, n+1):
            n = i
            while n > 0:
                if (n % 2) == 1:
                    answer[i] += 1

                n = n >> 1;

        return answer
        
        
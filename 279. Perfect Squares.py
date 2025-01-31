class Solution:
    def numSquares(self, n: int) -> int:
        if(isqrt(n) ** 2 == n):
            return 1
        while( n % 4 ==0):
            n /= 4        
        if(n %8 ==7):
            return 4
        
        i=1
        while(i*i <=n):   
            b = int(sqrt(n - i*i))
            if(b*b == (n - i*i)):
                return 2
            i += 1
        return 3
class Solution:
    def nthFibonacci(self, n):
        # code here
        if(n==1 or n==2):
            return 1
        a=1
        b=1
        for i in range(2,n):
            c=(a+b)%1000000007
            a=b%1000000007
            b=c
        return c
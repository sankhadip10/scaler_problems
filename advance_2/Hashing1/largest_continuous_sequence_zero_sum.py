class solution:
    def lszero(self,A):
        # A = [1, 2, -2, 4, -4]
        n = len(A)
        res = []
        for i in range(n):
            sum = 0
            for j in range(i,n):
                sum += A[j]
                if sum == 0:

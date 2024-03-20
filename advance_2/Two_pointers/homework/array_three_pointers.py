class solution:
    def solve(self,A,B,C):

        ans = float('inf')
        for i in range(len(A)):
            for j in range(len(B)):
                for k in range(len(C)):
                    val1 = abs(A[i] - B[j])
                    val2 = abs(B[j] - C[k])
                    val3 = abs(C[k] - A[i])
                    max_diff = max(val1,val2,val3)

                    # Update the answer if this combination has a smaller maximum difference.
                    ans = min(ans, max_diff)

        return ans

s = solution()
A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]
res=s.solve(A,B,C)
print(res)
class Solution:
    def divisors(self,num):
        count = 0
        for i in range(1,int(num ** 0.5)+1):
            if num % i == 0:
                count +=1 if i==num//i else 2
        return count

    def solve(self,A):
        n = len(A)
        res = []
        for i in range(n):
            val=self.divisors(A[i])
            # print("----",val)
            res.append(val)
        return res

s =Solution()
result = s.solve(A=[2,3,4,5])
print(result)
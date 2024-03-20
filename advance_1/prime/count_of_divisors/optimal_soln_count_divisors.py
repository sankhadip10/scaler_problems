class Solution:
    def smallest_prime_factor(self, A):
        spf_ = [i for i in range(A + 1)]

        for i in range(2, int(A ** 0.5) + 1):
            if spf_[i] == i:
                for j in range(i * i, A + 1, i):
                    if spf_[j] == j:
                        spf_[j] = i
        return spf_


    def solve(self, A):
        spf = self.smallest_prime_factor(max(A) + 1)
        print("+++++++++",spf)
        result = []
        for num in A:
            print("++",num)
            total = 1
            while num > 1:
                p = spf[num]
                count = 0
                while num % p == 0:
                    count += 1
                    num //= p
                total *= (count + 1)
            result.append(total)
        return result

s=Solution()
A=[12,56]
val=s.solve(A)
print(val)

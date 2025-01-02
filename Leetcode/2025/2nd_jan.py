class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # vowels = {'a','e','i','o','u'}
        # ans = []

        # for li,ri in queries:
        #     count = 0

        #     for i in range(li,ri+1):
        #         word = words[i]

        #         if word[0] in vowels and word[-1] in vowels:
        #             count += 1

        #     ans.append(count)
        # return ans

        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(words)
        prefix = [0] * n

        # Build the prefix sum array
        for i in range(n):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                prefix[i] = 1 if i == 0 else prefix[i - 1] + 1
            else:
                prefix[i] = 0 if i == 0 else prefix[i - 1]

        # Answer the queries
        ans = []
        for li, ri in queries:
            if li == 0:
                ans.append(prefix[ri])
            else:
                ans.append(prefix[ri] - prefix[li - 1])

        return ans

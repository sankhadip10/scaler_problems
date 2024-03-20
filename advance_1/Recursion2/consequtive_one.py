# Function to compute factorial without using the built-in factorial
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Function to calculate the rank of the string with repetition of characters
def find_rank_with_repetition(s):
    rank = 1
    n = len(s)

    # Custom function to count the frequency of each character in the string
    def count_chars(str):
        count = {}
        for char in str:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        return count

    # Calculate the count of each character in the string
    char_count = count_chars(s)

    # Calculate the rank of the string
    for i in range(n):
        cnt = 0
        for j in range(i + 1, n):
            if s[i] > s[j]:
                cnt += 1

        # Calculate the divisor considering the repetitions of characters
        div_factor = 1
        for char in char_count:
            print(char)
            div_factor *= factorial(char_count[char])
        print("+++",div_factor)
        print("+++++++++++++++++++++++++++++")

        rank += cnt * factorial(n - i - 1) // div_factor

        # Decrease the count of the current character
        char_count[s[i]] -= 1
        if char_count[s[i]] == 0:
            del char_count[s[i]]

    return rank


# Given a string 'a', find its rank among its permutations with repetition.
string_to_find_rank = 'queue'
rank = find_rank_with_repetition(string_to_find_rank)
print(rank)

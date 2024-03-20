def generateBinaryStrings(N, s='', last_char='0'):
    if N == 0:
        print(s)
    else:
        # You can always append a '0'
        generateBinaryStrings(N - 1, s + '0')
        # Append a '1' only if the last character was not '1'
        if last_char != '1':
            generateBinaryStrings(N - 1, s + '1', '1')

# Example usage
N = 3  # Change this value to generate strings of different lengths
generateBinaryStrings(N)
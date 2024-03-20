def custom_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_original_array(gcd_array):
    # Sort the GCD array in descending order
    gcd_array.sort(reverse=True)

    # Hash map to store the frequency of each GCD
    freq_map = {}
    for g in gcd_array:
        freq_map[g] = freq_map.get(g, 0) + 1

    original = []

    for g in gcd_array:
        if freq_map[g] > 0:
            # This might be a number in the original array
            original.append(g)
            # Update the frequency map
            for o in original:
                ogcd = custom_gcd(g, o)
                if freq_map[ogcd] > 0:
                    freq_map[ogcd] -= 1

    return original

# # Example usage
# gcd_array = [2, 3, 6, 2, 6, 3]  # Example input
# original_array = find_original_array(gcd_array)
# print("Original Array:", original_array)

gcd_array = [10, 8, 2, 2, 2, 2, 2, 2,2]
original_array = find_original_array(gcd_array)
print("Original Array:", original_array)


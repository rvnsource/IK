def reverse_bits(n):
    reversed_n = 0
    num_bits = n.bit_length()  # Get the number of bits in the input number

    for i in range(num_bits):
        # Shift the reversed number to the left and add the least significant bit of 'n'
        reversed_n <<= 1
        reversed_n |= (n & 1)
        n >>= 1

    return reversed_n

# Example usage:
original_number = 13
reversed_number = reverse_bits(original_number)
print(f"Original Number: {original_number} (binary: {bin(original_number)})")
print(f"Reversed Number: {reversed_number} (binary: {bin(reversed_number)})")

def split_unique_characters(s):
    seen = set()        # To keep track of characters already seen
    substrings = []     # To store the resulting substrings
    current_substring = ""

    for char in s:
        if char not in seen:
            seen.add(char)
            current_substring += char
        else:
            substrings.append(current_substring)
            current_substring = char
            seen = {char}

    substrings.append(current_substring)
    return substrings

# Example usage:
input_string = "abacddce"
result = split_unique_characters(input_string)
print(result)  # Output: ['ab', 'ac', 'dd', 'ce']

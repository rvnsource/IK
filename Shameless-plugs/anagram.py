def isAnagram(s, t):

    if len(s) != len(t):
        return False

    for char in s:
        print(char)

    map = {}

    for char in s:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1
    print(map)

    for char in t:
        if char in map and map[char] !=0 :
            map[char] -= 1
        else:
            return False
    return True

# Driver code
str1 = "gramm"
str2 = "gramm"

# Function call
if (isAnagram(str1, str2)):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")


# This code is contributed by shinjanpatra

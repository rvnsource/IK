def isPalindrame(s: str):
    slen = len(s)
    l = 0
    r = slen-1

    while(r>=l):
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True

s = "abbbbbbba"
print(isPalindrame(s))

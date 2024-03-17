def isPalindrome(i):
    if i>=(len(s)/2):
        return True

    if s[i]!= s[len(s)-i-1]:
        return False

    return isPalindrome(i+1)
s="nitin"
print(isPalindrome(0))
def palindrome(s):
    return s[::-1] == s
    #return s == s[::-1]
    


print(palindrome('rocky'))
print(palindrome('madam'))
print(palindrome('nursesrun'))

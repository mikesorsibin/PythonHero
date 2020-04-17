import string

def ispangram(mystring,alphabet=string.ascii_lowercase):
    #return set(mystring.lower()) == set(alphabhet)
    return set(alphabet) == set(mystring.lower())


print(ispangram("abcdefghijklmnoopqrstuvwxyzfsfjsdflksjdflksjf"))

print(ispangram("My name is michael cor sibin and i have dont not"))

print(ispangram("abcdefghijklmnoopqrstuv wxyzfsfjsdflksjdflksjfabcdefghijklmnopqrstuvw"))

print(ispangram("The quick brown fox jumps over the lazy dog"))

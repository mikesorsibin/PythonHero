def up_low(s):
    uppercount =''
    lowercount=''
    for letters in s:
        if letters.isupper():
            uppercount =uppercount +letters
    
        elif letters.islower():
            lowercount =lowercount +letters
    #print(f"No of upper case letters:{len(uppercount)}")
    #print(f"No of lower case letters:{len(lowercount)}")
    return f"No of upper case letters:{len(uppercount)}"
    return f"No of lower case letters:{len(lowercount)}"
    


print(up_low("Hello how are you I am INSIDE"))
print(up_low("Hello Mr. Rogers, how are you this fine Tuesday?"))
    

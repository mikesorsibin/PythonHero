def ask():
    while True:
        try:
            value = int(input("Enter a number to get its square:"))
            
        except ValueError:
            print("Error Occured please try again")
        else:
            print(f"The number squared is {value**2}")
            break


##def ask():
##    waiting =True
##    while waiting:
##        try:
##            value = int(input("Enter a number to get its square:"))
##            
##        except ValueError:
##            print("Error Occured please try again")
##        else:
##            print(f"The number squared is {value**2}")
##            waiting = False


ask()
        
        

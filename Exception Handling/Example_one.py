def ask_number():
    while True:
        try:
            result = int(input("Enter only a number:"))
        except:
            print("The input provided is not a number")
        else:
            print(f"Great you have given a number {result}")
            break
        finally:
            print("Whatever happens i will be displayed in the screen")
            print("I am going to ask you again if it is not an integer \n")

ask_number()

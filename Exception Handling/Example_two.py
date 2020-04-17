try:
    result = 10 +10
except TypeError:
    print("Kindly two valid numbers to add!")
except OSError:
    print("Other error have occured")
else:
    print("Add went well")
    print(result)
finally:
    print("I will get executed if it has happened or not")




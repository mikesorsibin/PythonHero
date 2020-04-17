try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("Exception handled.Its an zero division error")
finally:
    print("All done")

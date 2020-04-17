try:
    f = open("myfile","r")
    f.write("I have created a file")
except OSError
    print("There was error writing to file")
else:
    print("File has been created or amended")
finally:
    f.close()
    print("Thank you")

def print_big(letters):
    patterns = {1:'*',2:'**',3:'***'}
    alphabets = {'A':[3,2,1],'B':[1,3,2]}
    for pattern in alphabets[letters.upper()]:
        print(patterns[pattern])

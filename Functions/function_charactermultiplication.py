'''mystring = 'Hello'
new=''

for i in mystring:
    new = new+i*3
print(new)'''



def paper_doll(name):
    new=''
    for i in name:
        new+= i*3
    return new

print(paper_doll('hello'))
        

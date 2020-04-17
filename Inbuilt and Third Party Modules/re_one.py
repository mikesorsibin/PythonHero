import re

# List of patterns to search for
patterns = ['term1', 'term2']

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print('Searching for "%s" in:\n "%s"\n' %(pattern,text))
    
    #Check for match
    if re.search(pattern,text):
        print('Match was found. \n')
    else:
        print('No Match was found.\n')


'''
words= 'i am michael cor sibin and my id is michaelcorsbin@gmail.com'
>>> re.split('@',words)
['i am michael cor sibin and my id is michaelcorsbin', 'gmail.com']
>>> re.findall('michael',words)
['michael', 'michael']
'''

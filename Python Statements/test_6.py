st = 'Create a list of the first letters of every word in this string'

'''lt=[x[0] for x in st.split()]'''

lt =[]
for words in st.split():
    lt.append(words[0])

print(lt)

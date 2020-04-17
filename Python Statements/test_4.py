st='Print every word in this sentence that has an even number of letters'
for letters in st.split():
	if len(letters)%2==0:
		print("even")
	else:
		print(letters)

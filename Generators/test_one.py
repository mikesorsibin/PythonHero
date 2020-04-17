def gensquares(n):
    for numbers in range(n):
        yield numbers**2


for x in gensquares(10):
    print(x)

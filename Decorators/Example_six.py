def hello():
    return 'Hi Mike'

def other(some_func):
    print('Other code runs here')
    print(some_func())


other(hello)

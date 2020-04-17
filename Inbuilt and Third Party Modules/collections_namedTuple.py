from collections import namedtuple


Cat = namedtuple('Cat','age,breed,name')

c = Cat(age=2,breed=False,name='smokey')


print(c.age)

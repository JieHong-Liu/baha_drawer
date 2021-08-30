import random

first = int(input("from:"))
second = int(input("to:"))
how_many = int(input("how many:"))
random.seed()

x = random.sample(range(first, second+1), how_many)
print(x)

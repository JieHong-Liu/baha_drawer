import random

random.seed()
first = int(input("From:"))
second = int(input("TO:"))
how_many = int(input("How Many:"))

x = random.sample(range(first, second+1), how_many)
x.sort()
print(x)

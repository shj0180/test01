
import random

def random_get():
    path  = random.random()
    return path
r1 = random_get()
r2 = random_get()
# print(r1)
# print(r2)



r4 = random.uniform(12, 15)

for i in range(10):
    print(round(random.uniform(0, 1))*100)


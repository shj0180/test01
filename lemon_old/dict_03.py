a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {

    'x' : 1,
    'y' : 2
}

print(a.items())
for k,v in a.items():
    print(k,v)


# Find keys in common
d1 = a.keys() & b.keys() # { 'x', 'y' }
# print(d1)

# Find keys in a that are not in b
# print(a.keys() - b.keys()) # { 'z' }

# Find (key,value) pairs in common
# print(a.items() & b.items()) # { ('y', 2) }

d3 = a.items() - b.items()
# print(d3)
# print(type(d3))

# for i in a:
#     print(i)










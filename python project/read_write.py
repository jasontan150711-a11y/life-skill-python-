a = open('a10.txt','r')
print(a.read())

a = open('a10','r')
airplane = a.read()
print(airplane)

a = open('pi','r')
pn = a.read(4)
print(pn)

pn += a.read(5)
print(pn)


""" name='ShaikDadapeer'
lname='B.tech'
fname=name+lname
print(name[12])
print(name[-13])
print(len(name))
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.swapcase())
print(name.count(name))
print(name+lname)

#slicing
print(fname[::])
#print(name[0:4+1])
print(name[0:5])
print(name[5:14])
print(lname[0:14])
print(fname[::2])
print(fname[::-1]) """
maps='polygon(434.5466,52525.5425)'
x=maps.lstrip('polygon(')
y=x.rstrip(')')
result=y.split(',')
print(result)
long=result[0]
lati=result[1]
print('longitude= ',long)
print('latitude= ',lati)






# function without para meter
'''def add():
    a=int(input("enter a"))
    b=int(input('enter b'))
    print(a+b)
add()'''

# fun with one para meter
'''def wish(a):
    print("Good Morning! ",a)
wish('dadapeer')'''


# fun with multiple  para meter
'''
# def add(a,b,c):
#     print(a+b)
#     print(b+c)
#     print(a,b,c)
# add(2,3,5)

# fun with default values
def add(a,b,c=6):
     print(a+b)
     print(b+c)
     print(a,b,c)
add(2,3)

# dirctly we can assign values
def add(a,c=6,b=2):
    print(a + b)
    print(b + c)
    print(a, b, c)
add(c=2,b=3,a=2) 

#     *extra
def add(a,b,c,*extra):
    print(a + b)
    print(b + c)
    print(extra)
    print(a, b, c)
add(2,3,4,'dadapeer',5.6)#adding extra info and printimg that extra
'''

#FUNCTION WITH RETURN VALUES
# def add(n1,n2,n3):
#     sum =n1+n2+n3
#     return sum
# total =add(5,10,100)
# print(total)

# with multiple returns
'''def manuplations(a,c):
    s=a+c
    m=a*c
    d=a/c
    return s,m,d
a=(manuplations(10,20))
print(a)
print(a[1])# separate accessing of multiplication '''

#lambda function
a=lambda money:money+money
double=a(100)
print(double)

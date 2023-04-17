
###############  lists #################


#accepting list from user
"""n=int(input())
l=[]
for i in range(n):
    lists=int(input())
    l.append(lists)
print(l)"""

#some list operations

"""liste=['Dadapeer',2,3.14,'True']
print(liste)
print(liste[1:3])
name=['farak','hulk','thor']
liste.append(name)
i='hero'
liste.append(i)
print(liste)
liste.insert(2,'badigadi')
print(liste)
liste.pop()
print(liste)
liste.pop(5)
print(liste)
num=[1,5,8,0,1,45,6]
num.sort()
print(num)"""

# basic functions
#n=int(input())
lenth=int(input('enter the length of arry'))
arr=[]
for i in range(lenth):
    inp=int(input("enter the num"))
    arr.append(inp)
h=0
el=[]
for i in arr:
    if(i>h):
        e=i-h
        h=h+e
        el.append(e)
    else:
        h=i
        el.append(0)
        continue
print(sum(el))

"""print(salary)
print('min salary= ',min(salary))
print('max salary= ',max(salary))
print('sum of  salary= ',sum(salary))
salary.sort()
print("accending order",salary)
print("decending order",salary[::-1])"""

# adding two lists
# ?boys=['farak','badi','appanna']
# ls=['kajal','samantha','tammu']
# print('temp join ',boys+girls)
################################
# boys.extend(girls)
# print('permanent ',boys)

# Read mode
f = open('D:\\1.manac\\python\\citiesss.txt', mode='r')
#print(f.read())
print(f.readline(3))
city=f.read()
final_cities=city.split(',')
print(final_cities)

# write mode
'''f = open('D:\\1.manac\\python\\python.txt', mode='w')
f.write('haaiii dadapeer how r u ')
print('new data will added ')'''

# append
'''f = open('D:\\1.manac\\python\\python.txt', mode='a')
f.writelines('\n hope your doing well')'''
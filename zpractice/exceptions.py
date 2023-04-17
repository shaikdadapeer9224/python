# try , except , finally
'''
try:
    f=open('E:\\python.txt',mode='r')
    print(f.read())
except:
    f = open('D:\\1.manac\\python\\python.txt', mode='r')
    print(f.read())
finally:
    f.close()'''

############# raise

class ToYoungError(Exception):
    def __init__(self):
        print('wait for few more years ')
class ToOldError(Exception):
    def __init__(self):
        print('diffucult to get match in this age ')
if __name__ == '__main__':
    age=int(input())
    if age < 22:
        raise ToYoungError
    elif age >40:
        raise ToOldError
    else:
        print('match details share to u shortly')
f = open('sample.txt','r')
s1 = f.read(5)
print(s1)
print('*'*50)
s2 = f.read(10)
print(s2)
print('*'*50)
s3 = f.read(15)
print(s3)
f.close()
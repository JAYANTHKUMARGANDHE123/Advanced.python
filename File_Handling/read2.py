f = open('sample.txt','r')
s = f.read(5)
print(s)
s1 = f.read()
print('-'*50)
print(s1)
f.close()
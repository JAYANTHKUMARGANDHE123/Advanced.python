f = open('sample.txt','r')
print('is this file readable :',f.readable())
print('is this file writable :',f.writable())
f.close()
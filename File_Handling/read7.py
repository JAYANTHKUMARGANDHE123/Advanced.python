f = open('sample.txt','r')
count = 0
for line in f:
    count = count + 1
else:
    print('line count :',count)
f.close()
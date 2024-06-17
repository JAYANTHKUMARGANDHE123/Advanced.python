f = open('sample.txt','r')
line_number = 2
s = f.readlines()[line_number-1]
print(s)
f.close()
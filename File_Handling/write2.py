f = open('names.txt','w')
l = ['srikanth\n','jagadeesh\n','srinath\n']
#l = [str(10),str(20),str(30),str(40),str(50)]
f.writelines(l)
f.close()
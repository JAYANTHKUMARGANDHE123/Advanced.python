f = open('prime_number.py','w')
code ='''
num = input('please enter int value : ')
if num.isdigit() == True:
    num = int(num)
    for i in range(2,num):
        if num%i == 0:
            print(num,'is not a prime number')
            break
    else:
        print(num,'is a prime number')
else:
    print('Invalid input data')
'''
f.write(code)
f.close()
import test1

x = 10
def f1():
    print('f1 function definition')
    print('module name :',__name__)


if  __name__ == '__main__':
    print('Execution started from test.py')
    print(x)
    f1()
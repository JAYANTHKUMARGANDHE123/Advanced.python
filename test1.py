x = 20
def f1():
    print('f1 function definition')
    print('module name :',__name__)


if __name__ == '__main__':
    print('Execution started from test1.py')
    print(x)
    f1()
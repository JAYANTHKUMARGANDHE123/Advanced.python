from calculator import arithmetic
from calculator import logical

if __name__ == '__main__':
    print(arithmetic.addition(10,20))
    print(arithmetic.sub(10,20))
    print(arithmetic.difference(10,20))
    print(arithmetic.square(10))
    print(arithmetic.cube(10))
    print(logical.land(100,500))
    print(logical.lor(100,500))
    print(logical.lnot(100))
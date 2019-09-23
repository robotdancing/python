#! /usr/bin/python3
# _*_ coding=UTF-8 _*_

class MyError(Exception):
    def __init__(self):
        pass
    
    def __str__(self):
        return 'this is self define error'


def exp_exception(x, y):
    try:
        a = x / y
        raise MyError
        print('a=', a)
        return a
    except (ZeroDivisionError, NameError, MyError) as e:
        print(e)
    else:
        print('it goes as expect')
    finally:
        print('you will see this whatever happen')


exp_exception(2, 9)

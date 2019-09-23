#! /usr/bin/python3
# _*_ coding:UTF-8 _*_

import time

t = (2019, 9, 25, 17, 35, 38, 6, 48, 0)
print('%f' % time.time())
print('time.localtime:', time.localtime(time.time()))
print('time.gmtime():', time.gmtime())
print('time.mktime(): %f' % time.mktime(t))
print('time.asctime(): %s' % time.asctime(time.localtime()))
print('time.ctime(): %s' % time.ctime())
time.sleep(5)
print('time.ctime(): %s' % time.ctime())

def procedure():
    time.sleep(2)
t1 = time.process_time()
procedure()
print('second process time:', time.process_time())

t2 = time.time()
procedure()
print('second wall time:', time.time()-t2)
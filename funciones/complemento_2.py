#!/usr/bin/python3
def com2(a):
    b = ''
    pot = 0
    res = 0
    print(a)
    for i in a:
        if i == '1':
            b += '0'
        else:
            b += '1'
    for i in reversed(b):
        res += ((int(i) * 2) ** pot)
        pot += 1
    res += 1
    print('{0:016b}'.format(res))
    return '{0:016b}'.format(res)

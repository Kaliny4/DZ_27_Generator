"""
Создать генератор геометрической прогрессии
"""
# bn = bn-1*q, где q — знаменатель прогрессии.


def geom_progr(num, znamennyk, max):
    if znamennyk == 0:
        raise TypeError
    elem = num / znamennyk
    while max >= elem:
        elem *= znamennyk
        yield elem


a = geom_progr(2, 0, 100)
try:
    for item in a:
        print(item)
except TypeError:
    print('znamennyk cant be zero')



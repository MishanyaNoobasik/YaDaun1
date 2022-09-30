def make_looper(string):
    import os
    f = open('t.txt', 'a')
    f.write('1')
    f.close()
    stat = os.stat('t.txt')
    print(stat.st_size)
    a = stat.st_size % len(string)
    return string[a - 1]


a = '12aerhetntntrnrtanatenate3'
print(make_looper(a))

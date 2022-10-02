# def make_looper_file(string):
#     import os
#     f = open('t.txt', 'a')
#     f.write('1')
#     f.close()
#     a = os.stat('t.txt').st_size % len(string)
#     return string[a - 1]
#
#
# a = 'abc'
# print(make_looper_file(a))


def counter(func):
    def wrapper(stri):
        wrapper.count += 1
        func(stri)
        res = stri[(wrapper.count - 1) % len(stri)]
        return print(res)
    wrapper.count = 0
    return wrapper


@counter
def make_looper(string):
    return string


a = make_looper('abc')
make_looper('abc')
make_looper('abc')
make_looper('abc')
make_looper('abc')
make_looper('abc')

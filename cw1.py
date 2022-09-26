# def to_jaden_case(string):
#     word = string.split(' ')
#
#     for el in range(len(word)):
#         word[el] = word[el].capitalize()
#
#     res = ' '.join(word)
#     return res
#
#
# a = 'ya yebu sobak, vsegda gotov'
# print(to_jaden_case(a))


# def open_or_senior(data):
#     res = []
#     for i in data:
#         if int(i[0]) >= 55 and i[1] in range(8, 27):
#             res.append('Senior')
#         elif i[0] > 0 and i[1] in range(-2, 27):
#             res.append('Open')
#         else:
#             res.append('Error')
#     return res
#
# data = [[18, 20], [45, 2], [-1, 12], [37, 6], [21, 21], [78, 9]]
# print(open_or_senior(data))

# def get_sum(a, b):
#     if b > a:
#         res = 0
#         for i in range(a, b+1):
#             res += i
#
#     else:
#         res = 0
#         for i in range(b, a + 1):
#             res += i
#     return res
#
#
# print(get_sum(1, -5))

n = 0
print(n)


def whitespace_number(n):
    z = ''
    if n > 0:
        z = ' '
    elif n < 0:
        z = '\t'
    else:
        pass
    r = ''
    a = abs(n)
    if a != 0:
        while a > 0:
            r = str(a % 2) + r
            a //= 2
        r1 = r.replace('0', ' ')
        r2 = r1.replace('1', '\t')
        res = z + r2 + '\n'
    else:
        res = ' \n'
    return res


print(whitespace_number(n))

mass = [1, 1, -1, 4, 4, 4, 5, 6]
n = 3


def count_contiguous_distinct(k, arr):
    if len(arr) >= k:
        a = 0
        b = k - 1
        res = []
        mas = []
        while a < len(arr) - k + 1:
            for i in range(a, b + 1):
                mas.append(arr[i])
            # mas.sort()
            # c = 1
            # for i in range(1, len(mas)):
            #     if mas[i] != mas[i - 1]:
            #         c += 1
            c = set(mas)
            res.append(len(c))
            a += 1
            b += 1
            mas.clear()
    else:
        res = 'Error'
    return res


print(count_contiguous_distinct(n, mass))
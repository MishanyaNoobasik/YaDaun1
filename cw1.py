from datetime import datetime
n = 13000
mass = [1, 1, 2, 4, 7, 8, 10, 4, 13, 1, 10, 1, 1] * 10000


def count_contiguous_distinct(k, arr):
        mas = []
        for el in range(k):
            mas.append(arr[el])
        res = [(len(set(mas))), ]
        a = 0
        while a < len(arr) - k:
            mas.append(arr[a + k])
            mas.pop(0)
            res.append(len(set(mas)))
            a += 1
        return res


start_time = datetime.now()
print(count_contiguous_distinct(n, mass))
time1 = datetime.now() - start_time

print('Ya: ', time1)



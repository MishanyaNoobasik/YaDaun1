# # Классы и объекты
#
# class Point:
#     "Класс для представления координат точек на плоскости"
#     color = 'red'
#     circle = 2
#     pass
#
#
# Point.color = 'black'
# print(Point.__dict__)                          # чтоб увидеть все аттрибуты класса
# a = Point()
# b = Point()
#
# print(type(a))
# print(type(a) == Point)
#
# Point.circle = 1
# a.color = 'green'
# print(a.__dict__)
# Point.type_pt = 'disc'                          # добавление аттрибутов
# setattr(Point, 'prop', 1)
# print(Point.__dict__)
# print(getattr(Point, 'color', False))
# del Point.prop
# print(hasattr(Point, 'prop'))
# delattr(Point, 'type_pt')
# print(hasattr(a, 'circle'))
# try:
#     del a.circle
# except AttributeError:
#     print('debil?')
#
# a.x = 1
# a.y = 2
#
# b.x = 10
# b.y = 2
#
# print(Point.__doc__)
#


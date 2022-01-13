import math
import random
from builtins import float


# Функция преобразует градусы в радианы
def to_rad(deg: float):
    return deg * math.pi / 180


# Функция преобразует радианы в градусы
def to_grad(rad: float):
    return rad * 180 / math.pi

# Задание 1
# grad = float(input('Введите градусы: '))
# print('Радианы: ', to_rad(grad))


# ЗАДАНИЕ 2
# radian = float(input('Введите радианы: '))
# print('Градусы: ', to_grad(radian))


# ЗАДАНИЕ 3
# Функция рассчитывает площадь трапеции по двум сторонам и высоте
# def calc_area_trapezoid(a: float, b: float, h: float):
#     return a * b * h / 2
#
#
# a = float(input('Введите сторону "a": '))
#
# b = float(input('Введите сторону "b": '))
#
# h = float(input('Введите высоту трапеции "h": '))
#
# print(calc_area_trapezoid(a, b, h))


# ЗАДАНИЕ 4
# Функция рассчитывает площадь трапеции по двум сторонам и высоте
# def calc_area_trapezoid(side1: float, side2: float, deg: float):
#     return math.sin(to_rad(deg)) * side1 * side2
#
#
# a = float(input('Введите сторону "a": '))
#
# b = float(input('Введите сторону "b": '))
#
# alfa = float(input('Введите угол у основания трапеции "alfa": '))
#
# print(calc_area_trapezoid(a, b, alfa))


# ЗАДАНИЕ 5
# Функция рассчитывает площадь поверхности цилиндра по высоте и радиусу
# def calc_area_cyl(height_cyl: float, radius_cyl: float):
#     return 2 * math.pi * radius_cyl * height_cyl + 2 * math.pi * (radius_cyl ** 2)
#
#
# # Функция рассчитывает объем цилиндра по высоте и радиусу
# def calc_volume_cyl(height_cyl: float, radius_cyl: float):
#     return math.pi * height_cyl * (radius_cyl ** 2)
#
#
# height = float(input('Введите высоту цилиндра: '))
#
# radius = float(input('Введите радиус цилиндра: '))
#
# print('Площадь полной поверхности цилиндра: ', calc_area_cyl(height, radius))
# print('Объем цилиндра: ', calc_volume_cyl(height, radius))


# ЗАДАНИЕ 6
# Функция рассчитывает объем сферы радиуса r
# def calc_area_sphere(radius_sphere: float):
#     return 4 * math.pi * (radius_sphere ** 2)
#
#
# # Функция рассчитывает площадь поверхности сферы радиуса r
# def calc_volume_sphere(radius_sphere: float):
#     return 4 * math.pi * (radius_sphere ** 2) / 3
#
#
# radius = float(input('Введите радиус сферы: '))
#
# print('Площадь поверхности сферы: ', calc_area_sphere(radius))
# print('Объем сферы: ', calc_volume_sphere(radius))

# ЗАДАНИЕ 7
# Функция рассчитывает длину дуги окружности радиуса r и угла дуги deg
# def calc_arc_length(radius_circle: float, deg: float):
#     return math.pi * radius_circle * deg / 180
#
#
# radius = float(input('Введите радиус окружности: '))
#
# grad = float(input('Введите угол дуги: '))
#
# print('Длина дуги: ', calc_arc_length(radius, grad))


# ЗАДАНИЕ 8
# Функция рассчитывает площадь сектора окружности радиуса r и угла дуги deg
# def calc_area_sector(radius_circle: float, deg: float):
#     return to_rad(deg) * (radius_circle ** 2) / 2
#
#
# radius = float(input('Введите радиус окружности: '))
#
# grad = float(input('Введите угол дуги: '))
#
# print('Площадь сектора: ', calc_area_sector(radius, grad))


# ЗАДАНИЕ 9
# Функция принимает число относительно которого расчитываем кратность и остальные аргументы цифры
# def get_first_multiple(multiplicity: int, *nums: int):
#     for n in nums:
#         if n % multiplicity == 0:
#             return n
#
#     return 'Число кратное ' + str(multiplicity) + ' не найдено'
#
#
# num = int(input('Введите число, относительно которого будет рассчитываться кратность: '))
#
# entered_list = input("Введите список чисел, разделенных пробелом: ").split()
#
# num_list = [int(i) for i in entered_list]
#
# print(get_first_multiple(num, *num_list))


# ЗАДАНИЕ 10
# Функция рассчитывает сумму квадратов n чисел
# def calc_sum_of_squares(*nums: int):
#     result = 0
#     for n in nums:
#         result += n ** 2
#
#     return result
#
#
# # Функция рассчитывает квадрат суммы n чисел
# def calc_squares_of_sum(*nums: int):
#     result = 0
#     for n in nums:
#         result += n
#
#     return result ** 2
#
#
# # Функция рассчитывает разницу между квадратом суммы и суммы квадратов первых n чисел
# def calc_difference_between_nums(num1, num2):
#     return num1 - num2
#
#
# entered_list = input("Введите список чисел, разделенных пробелом: ").split()
#
# num_list = [int(i) for i in entered_list]
#
# print(
#     'Разница между квадратом суммы и суммы квадратов введенных чисел: ',
#     calc_difference_between_nums(calc_sum_of_squares(*num_list), calc_squares_of_sum(*num_list)),
# )


# ЗАДАНИЕ 11
# Функция умножает два целых числа без использования оператора "*"
# def multiplication(value1: int, value2: int):
#     result: int = 0
#     for n in range(value2):
#         result += value1
#
#     return result
#
#
# v1 = int(input("Введите первое число: "))
#
# v2 = int(input("Введите второе число: "))
#
# print(multiplication(v1, v2))


# ЗАДАНИЕ 12
# Функция рассчитывает расстояние между двумя точками по широте и долготе
# def distance(lat1, lon1, lat2, lon2):
#     r = 6371
#     d_lat = to_rad(lat2 - lat1)
#     d_lon = to_rad(lon2 - lon1)
#     a = math.sin(d_lat / 2) * math.sin(d_lat / 2) + math.cos(to_rad(lat1)) * math.cos(to_rad(lat2))\
#         * math.sin(d_lon / 2) * math.sin(d_lon / 2)
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#     d = r * c
#     return d
#
#
# lat_1 = int(input("Введите широту 1: "))
# lon_1 = int(input("Введите долготу 1: "))
# lat_2 = int(input("Введите широту 2: "))
# lon_2 = int(input("Введите долготу 2: "))
#
# print("Расстояние: ", distance(lat_1, lon_1, lat_2, lon_2))


# ЗАДАНИЕ 13
# def area(n: int, a: float):
#     return n * (a ** 2) / (4 * math.tan(to_rad(180 / n)))
#
#
# num = int(input("Введите кол-во сторон (целое число): "))
# length = int(input("Введите длину стороны: "))
#
# print("Площадь многоугольника с кол-вом сторон = " + str(num) + " равно ", area(num, length))


# ЗАДАНИЕ 14
# def format_num(a: float):
#     return bin(a)[2:]
#
# num = int(input("Введите число в десятичном формате: "))
#
# print("Двоичное число = " + str(format_num(num)))


# ЗАДАНИЕ 15
# Преобразовать в полярные координаты
# def to_polar(x: int, y: int):
#     r = math.sqrt(abs(x) ** 2 + abs(y) ** 2)
#     if r == 0:
#         return 0.0
#     rad = math.acos(x / r)
#     deg = to_grad(rad)
#     if y < 0:
#         return 360 - deg
#     return to_grad(rad)
#
#
# coordinates = input("Введите координаты вектора через пробел: ").split()
#
# try:
#     int(coordinates[0])
#     int(coordinates[1])
# except IndexError:
#     print("Некорректное кол-во элементов")
# except ValueError:
#     print("Должны быть введены числа")
# else:
#     if len(coordinates) == 2:
#         print(to_polar(int(coordinates[0]), int(coordinates[1])))
#     else:
#         print("Некорректное кол-во элементов")


# ЗАДАНИЕ 16
# def format_num(a: float):
#     return round(a, 2)
#
#
# num = float(input("Введите число: "))
#
# print("Десятичное число = " + str(format_num(num)))


# ЗАДАНИЕ 17
# def throw_up(count: int):
#     eagles = 0
#     for i in range(count):
#         r = random.randint(0, 1)
#         if r:
#             eagles += 1
#     return eagles
#
#
# num = int(input("Введите число: "))
#
# print("Орлы = " + str(throw_up(num)))


# ЗАДАНИЕ 18
# def volume(a: float):
#     return math.sqrt(2) * (a ** 3) / 12
#
# num = int(input("Введите длину ребра тетрайдера: "))
#
# print("Объем тетрайдера = " + str(volume(num)))


# ЗАДАНИЕ 19
# def to_hex(a: int):
#     return hex(a)[2:]
#
# num = int(input("Введите число: "))
#
# print("hex = " + str(to_hex(num)))


# ЗАДАНИЕ 20
# def maximer(a: float, b: float):
#     if a > b:
#         return a
#     else:
#         return b
#
# def evclid_distance(nums1: tuple[float], nums2: tuple[float]):
#     max_length = maximer(len(nums1), len(nums2))
#     result = 0
#
#     for n in range(max_length):
#         sum = 0
#         if len(nums1) > n:
#             sum += nums1[n]
#         if len(nums2) > n:
#             sum -= nums2[n]
#         result += sum ** 2
#
#     return math.sqrt(result)
#
#
# entered_list1 = input("Введите чисел, определяющих первый вектор, разделенных пробелом: ").split()
# entered_list2 = input("Введите чисел, определяющих второй вектор, разделенных пробелом: ").split()
#
# num_list1 = [int(i) for i in entered_list1]
# num_list2 = [int(i) for i in entered_list2]
#
# print(evclid_distance(num_list1, num_list2))

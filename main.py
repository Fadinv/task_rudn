import math
from builtins import float


# Функция преобразует градусы в радианы
def toRad(deg: float):
    return deg * math.pi / 180


# Функция преобразует радианы в градусы
def toGrad(rad: float):
    return rad * 180 / math.pi


# # task 1
# grad = float(input('Введите градусы: '))
# print('Радианы: ', toRad(grad))
#
# # task 2
# radian = float(input('Введите радианы: '))
# print('Градусы: ', toGrad(radian))


# task 3
# Функция расчитывает площадь трапеции по двум сторонам и высоте
# def calcAreaTrapezoid(a: float, b: float, h: float):
#     return a * b * h / 2
#
#
# a = float(input('Введите сторону "a": '))
#
# b = float(input('Введите сторону "b": '))
#
# h = float(input('Введите высоту трапеции "h": '))
#
# print(calcAreaTrapezoid(a, b, h))


# task 4
# Функция расчитывает площадь трапеции по двум сторонам и высоте
# def calcAreaTrapezoid(side1: float, side2: float, deg: float):
#     return math.sin(toRad(deg)) * side1 * side2
#
#
# a = float(input('Введите сторону "a": '))
#
# b = float(input('Введите сторону "b": '))
#
# alfa = float(input('Введите угол у основания трапеции "alfa": '))
#
# print(calcAreaTrapezoid(a, b, alfa))


# task 5
# Функция расчитывает площадь поверхности цилиндра по высоте и радиусу
# def calcAreaCyl(height_cyl: float, radius_cyl: float):
#     return 2 * math.pi * radius_cyl * height_cyl + 2 * math.pi * (radius_cyl ** 2)
#
#
# # Функция расчитывает объем цилиндра по высоте и радиусу
# def calcVolumeCyl(height_cyl: float, radius_cyl: float):
#     return math.pi * height_cyl * (radius_cyl ** 2)
#
#
# height = float(input('Введите высоту цилиндра: '))
#
# radius = float(input('Введите радиус цилиндра: '))
#
# print('Площадь полной поверхности цилиндра: ', calcAreaCyl(height, radius))
# print('Объем цилиндра: ', calcVolumeCyl(height, radius))


# task 6
# Функция расчитывает объем сферы радиуса r
# def calcAreaSphere(radius_sphere: float):
#     return 4 * math.pi * (radius_sphere ** 2)
#
#
# # Функция расчитывает площадь поверхности сферы радиуса r
# def calcVolumeSphere(radius_sphere: float):
#     return 4 * math.pi * (radius_sphere ** 2) / 3
#
#
# radius = float(input('Введите радиус сферы: '))
#
# print('Площадь поверхности сферы: ', calcAreaSphere(radius))
# print('Объем сферы: ', calcVolumeSphere(radius))

# task 7
# Функция рассчитывает длину дуги окружности радиуса r и угла дуги deg
# def calcArcLength(radius_circle: float, deg: float):
#     return math.pi * radius_circle * deg / 180
#
#
# radius = float(input('Введите радиус окружности: '))
#
# grad = float(input('Введите угол дуги: '))
#
# print('Длина дуги: ', calcArcLength(radius, grad))


# task 8
# Функция рассчитывает площадь сектора окружности радиуса r и угла дуги deg
# def calcAreaSector(radius_circle: float, deg: float):
#     return toRad(deg) * (radius_circle ** 2) / 2
#
#
# radius = float(input('Введите радиус окружности: '))
#
# grad = float(input('Введите угол дуги: '))
#
# print('Площадь сектора: ', calcAreaSector(radius, grad))


# task 9
# Функция принимает число относительно которого расчитываем кратность и остальные аргументы цифры
# def getFirstMultiple(multiplicity: int, *nums: int):
#     for n in nums:
#         if n % multiplicity == 0:
#             return n
#
#     return 'Число кратное ' + str(multiplicity) + ' не найдено'
#
#
# num = int(input('Введите число, относительно которого будет расчитываться кратность: '))
#
# entered_list = input("Введите список чисел, разделенных пробелом: ").split()
#
# num_list = [int(i) for i in entered_list]
#
# print(getFirstMultiple(num, *num_list))


# task 10
# Функция расчитывает сумму квадратов n чисел
# def calcSumOfSquares(*nums: int):
#     result = 0
#     for n in nums:
#         result += n ** 2
#
#     return result
#
#
# # Функция расчитывает квадрат суммы n чисел
# def calcSquaresOfSum(*nums: int):
#     result = 0
#     for n in nums:
#         result += n
#
#     return result ** 2
#
#
# # Функция рассчитывает разницу между квадратом суммы и суммы квадратов первых n чисел
# def calcDifferenceBetweenNums(num1, num2):
#     return num1 - num2
#
#
# entered_list = input("Введите список чисел, разделенных пробелом: ").split()
#
# num_list = [int(i) for i in entered_list]
#
# print(
#     'Разница между квадратом суммы и суммы квадратов введенных чисел: ',
#     calcDifferenceBetweenNums(calcSumOfSquares(*num_list), calcSquaresOfSum(*num_list)),
# )


# task 11
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

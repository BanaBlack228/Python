# Типы данных

#Integer(int) - целые числа
a = 5
b = 6
c = a + b
d = a / b
print(c)
print(d)

#Float (float) - вещественные числа

float_a = 0.5
float_b = 1.25

print(type(a))
print(type(float_a))

#Boolean - Логический тип данных

is_active = True
is_logout = False

print(is_active or is_logout)
print(is_active and is_logout)
print(not is_active and is_logout)

print(a < b)
print(a > b)
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)


#name_of_person - пишем в стиле snakecase

age = '15'
year = '2024'
print(int(age) + int(year))

#String - (str) - строковый тип данных

text = "I Love Python"
text = text + 'a'
text += 'a'

#None

flag = None


#Структуры данных


#списки - list() - []

cars = ['bmw','audi', 24, True, [1,2]]

#Словари - dict() - {}
info = {
    'name': 'Alex',
    'cars': cars,
}

#кортежи - tuple - () - неизменяемый список

colors = (
    ('red','255,0,0'),
    ('blue','0,0,255')
)

#set - set() - множества - {}

set_numbers = {1,2,3,4,5}

#функции
#файлы
#классы

''' 
многострочный коментарий

'''

text_many_lines = """ 

многострочный текст

"""
# ввод данных из консоли
name = input("Введите свое имя ")
age = input("Введите свое возраст ")

print('Hello', name)
print('Тебе',age,'Лет')

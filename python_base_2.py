#Условное выражение
age = 21
if age < 20:
        print("error")
        if age < 15:
            print('FAAAATAAAALLLL!!!!')
        else:
            print('not fatal')
elif age < 25:
    print('<25')
else:
    print('ok')


print('Next')

#Цикл FOR

numbers = [1,2,3,4,5,6,7,8,9]
cars = ['bmw','audi','lada']
N = 10
# for i in range(1, N, 1):
#     print(i)

# for ind in range(len(cars)):
#     print(ind,cars[ind])

a = 10
b = 0
while a < 20:
    print(a)
    b += 1
    if b == 15:
        break
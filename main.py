#тут будет простой калькулятор#
num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
oper = input("Выберите и введите одну из операций + - :")

num1 = int(num1)
num2 = int(num2)
if oper == '+':
    result = num1 + num2
elif oper == '-':
    result = num1 - num2
else: result = 'Я не умею в такую операцию'
result = str(result)
print("Ответ: " + result)
#no comments#
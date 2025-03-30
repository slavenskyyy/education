print("Привет, это калькулятор!")

m = 'a'
count = 0
while m != '=':
    print('Ввод первого числа:')
    num1 = int(input())
    print('Ввод второго числа:')
    num2 = int(input())

    print('Если ты хочешь сложить числа, введи цифру "1"')
    print('Если ты хочешь вычесть числа, введи цифру "2"')
    print('Если ты хочешь умножить числа, введи цифру "3"')
    print('Если ты хочешь поделить числа, введи цифру "4"')

    number = int(input())


    if number == 1:
        count = count + (num1 + num2)
    elif number == 2:
        count = count + (num1 - num2)
    if number == 3:
        count = count + (num1 * num2)
    if number == 4:
        if num2 == 0:
            print("Делить на 0 нельзя!")
            break
        else:
            count = count + (num1 / num2)

    print(' Если ты хочешь узнать результат, введи "=" ')
    print(' Если ты хочешь продолжить вычисления, введи ВСЕ кроме "=" ')

    m = input()
    if m == '=':
        print("Ответ:" ,count)
    else:
        continue
import random

print('Привет! Сейчас сыграем в угадай число ;)')

s1,s2 = int(input("Введи левую границу диапозона"  )),int(input("Введи правую границу диапозона"  ))

n = random.randint(s1, s2)

def is_valid(x):

    return s1 <= x <= s2

start = 1

count = 0

while start == 1:

    while True:

        num = int(input(f'Я загадал число от {s1} до {s2}. Как ты думаешь какое это число? Твой вариант:  '))

        if not is_valid(num):

            print(f'А может быть все-таки введем целое число от {s1} до {s2}? ')

        else:

            while True:

                if num < n:

                    count +=1

                    num = int(input('Твое число меньше, чем я загодал, попробуй еще раз:  '))

                elif num > n:

                    count +=1

                    num = int(input('А это число больше загаданного, давай еще разок:  '))

                else:

                    print('Ураа! Ты угадал, поздравляю!')

                    print('Твое кол-во попыток: ', count)

                    count = 0

                    break

            break

    print('Спасибо, что сыграл со мной')

    start = int(input('''Может повторим?

(1 = да, 0 = нет)

 Твой ответ:   '''))

    if start ==1:
        s1,s2 = int(input("Введи левую границу диапозона"  )),int(input("Введи правую границу диапозона"  ))
        n = random.randint(s1, s2)

    else:

        print('Ну ладно :( Еще увидимся...')

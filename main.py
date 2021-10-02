from random import randint
print('угадай число от 1 до 100')
def next():
    while True:
        again = input('введите yes если хотите продолжить или любой символ что бы закончить')
        print()
        if again == 'yes':
            game()
        else:
            print("bb")
            break
def game():
    num = randint(1, 100)
    c = 0
    while True:
        igrok = is_digit(input())
        c += 1
        if igrok == num:
            break
        if igrok > num:
            print('слишком много')
        else:
            print('слишком мало')
    print('попыток=', c, 'число=', igrok)
def is_digit(num):
    if num.isdigit():
        return int(num)
    else:
        print('Введите число')
        return is_digit(input())
game()
next()

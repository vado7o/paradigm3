# Задача 2. Создайте программу для игры в ""Крестики-нолики"".

import os
os.system('cls')

line1 = ['-1-', '-2-', '-3-']
line2 = ['-4-', '-5-', '-6-']
line3 = ['-7-', '-8-', '-9-']
turn = 'O'

str_line = '+---+---+---+'

def print_line(line):
    for i in line:
        if i == 'O': print('| O ', end='')
        elif i == 'X': print('| X ', end='')
        else: print(f'|{i}', end='')
    print(f'|\n{str_line}')

def print_field():
    print(f'\n{str_line}')
    print_line(line1)
    print_line(line2)
    print_line(line3)

def check_horizontal(line):
    if ''.join(map(str, line)) == 'OOO': return 0
    elif ''.join(map(str, line)) == 'XXX': return 1

def check_vertical():
    for i in range(3):
        if line1[i] == line2[i] and line1[i] == line3[i] and line1[i] == 'O': return 0
        elif line1[i] == line2[i] and line1[i] == line3[i] and line1[i] == 'X': return 1

def check_diagonal():
    if line1[0] == line2[1] and line1[0] == line3[2] and line1[0] == 'O': return 0
    elif line1[0] == line2[1] and line1[0] == line3[2] and line1[0] == 'X': return 1
    elif line3[0] == line2[1] and line3[0] == line1[2] and line3[0] == 'O': return 0
    elif line3[0] == line2[1] and line3[0] == line1[2] and line3[0] == 'X': return 1

def check_win():
    if check_horizontal(line1) == 0 or check_horizontal(line2) == 0 or check_horizontal(line3) == 0 or check_vertical() == 0 or check_diagonal() == 0: return 0
    elif check_horizontal(line1) == 1 or check_horizontal(line2) == 1 or check_horizontal(line3) == 1 or check_vertical() == 1 or check_diagonal() == 1: return 1

def check_busy(line, num):
    if line[move - num] != 'X' and line[move - num] != 'O':
        line[move - num] = turn
        return True
    else:
        print('Указанная Вами клетка уже занята!!!\n')
        print_field()
        return False

def check_draw():
    sum = 0
    for i in range(3):
        if line1[i] == 'X' or line1[i] == 'O': sum += 1
        if line2[i] == 'X' or line2[i] == 'O': sum += 1
        if line3[i] == 'X' or line3[i] == 'O': sum += 1
    return sum

while True:
    print_field()

    if check_win() == 1 or check_win() == 0:
        print(f'\nВыиграли {turn} !!!\n')
        break

    if check_draw() == 9:
        print('\nНИЧЬЯ !!!\n')
        break

    if turn == 'X': turn = 'O'
    else: turn = 'X'

    while True:
        try:
            move = int(input(f'\nВведите номер клетки куда нужно поставить {turn}: '))
            if move in range(1, 10):
                if 1 <= move <= 3:
                    if not check_busy(line1, 1):
                        continue
                elif 4 <= move <= 6:
                    if not check_busy(line2, 4):
                        continue
                else:
                    if not check_busy(line3, 7):
                        continue
                break

            else:
                print('Номер клетки должен находиться в диапазоне 1..9 !!!\n')
                print_field()
        except:
            print('Неверно указан номер клетки!\n')
            print_field()
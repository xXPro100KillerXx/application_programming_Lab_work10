k = [64, 32, 16, 8, 4, 2, 1]
s = - 1

while s == -1:                  # цикл для ввода числа и обработка ошибок
    s = int(input('Введите натуральное число:'))
    if s <= 0:
        print('Ошибка! Необходимо ввести натуральное число')
        s = -1

for i in k:                     # поиск в списке нужных купюр и вывод их количества в консоль
    num = s // i
    s -= (num * i)
    if num != 0:
        print(f'{num} куп. номиналом: {i}')
    if s == 0:
        break
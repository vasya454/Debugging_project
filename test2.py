def power(x: float, n: int):
    z = 1
    if n > 0:
        for i in range(1, n + 1):
            z = z * x
        return z


if __name__ == '__main__':
    try:
        x = input('Введите x: ')
        if 0 <= x <= 999:
            n = int(input('Введите n: '))
            if 0 <= n <= 100:
                print(f'{x} в степени {n} равно {power(x, n)}')
            else:
                print('Ошибка, n  должен быть в диапазоне [1..100]')
        else:
            print('Ошибка, x  должен быть в диапазоне [1..999]')
    except:
        print('Ошибка, нужно ввести числовое значение')

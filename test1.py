def power(x: float, n: int):
    z = 1
    if n > 0:
        for i in range(1, n + 1):
            z = z * x
        return z
    else:
        print('Ошибка! Степень n должна быть целым положительным числом')


if __name__ == '__main__':
    #print(power(2, 0))
    print(str.find('ffggggdjl', 'j'))
    print('ffggggdjl'.find('j'))

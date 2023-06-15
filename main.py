def multiplication(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Введены параметры неправильного типа')
    else: return a * b


def division(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Введены параметры неправильного типа')
    else:
        try:
            return a / b
        except ZeroDivisionError:
            raise TypeError('Деление на 0')


def main():
    try:
        print(multiplication(2, 3))
        print(division(3, 0))
        print(division('dfdf', 5))
    except TypeError as e_type:
        print(e_type)
    except ZeroDivisionError as e_zero:
        print(e_zero)


if __name__ == '__main__':
    main()

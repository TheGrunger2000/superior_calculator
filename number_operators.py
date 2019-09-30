# Superior Calculator v 0.1.0
# Created by TheGrunger2000
# E-mail: grungerdiary@gmail.com
from decimal import Decimal


def summate(*args):  # 2 + 3 = 2 + 1 + 1 + 1 = 5
    input_data = []
    for number in args:
        input_data.append(Decimal(str(number)))
    answer = 0
    for term in input_data:
        answer += term
    return str(answer)


def multiplicate():  # 2 * 3 = 2 + 2 + 2 = 6
    pass


def exponentiate():  # 2 ** 3 =  2 * 2 * 2 = 8
    pass


def tetrate():  # 2 ^^ 3 = 2 ** 2 ** 2 = 16
    pass


def pentate():  # 2 ^^^ 3 = 2 ^^ 2 ^^ 2 = 65 536
    pass


def hyperoperate():
    pass


if __name__ == "__main__":
    a = summate(2, 3, 4, 5, 6, 456735675467453456734535674567435673457.456734567, .345634563456345635)
    print(a)

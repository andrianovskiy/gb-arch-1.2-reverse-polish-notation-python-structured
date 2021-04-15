from reverse_polish_notation.constants import ADD
from reverse_polish_notation.constants import SUBTRACK
from reverse_polish_notation.constants import MULTIPLY
from reverse_polish_notation.constants import DIVIDE
from reverse_polish_notation.checktype import isfloat


# Расчет значения по выражению в обратной польской записи
def calculate_reverse_polish(expression):
    queue = [] + [0]
    for lex in expression:
        sub = 0
        if lex.isdigit():
            queue = [int(lex)] + queue
            continue
        elif isfloat(lex):
            queue = [float(lex)] + queue
            continue
        elif len(queue) < 2:
            err = "Ошибка! Некорректное выражение"
            print(err)
            return "", err
        elif lex == ADD:
            sub = add(queue[1], queue[0])
        elif lex == SUBTRACK:
            sub = subtrack(queue[1], queue[0])
        elif lex == MULTIPLY:
            sub = multiply(queue[1], queue[0])
        elif lex == DIVIDE:
            sub = divide(queue[1], queue[0])
        queue = queue[1:]
        queue[0] = sub
    return round(queue[0], 6), ""

def add(value1, value2):
    return value1 + value2

def subtrack(value1, value2):
    return value1 - value2

def multiply(value1, value2):
    return value1 * value2

def divide(value1, value2):
    if (value2 == 0):
        err = "Ошибка! Деление на 0"
        print(err)
        return "", err
    return value1 / value2, ""
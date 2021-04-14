import sys
from reverse_polish_notation.transfom import to_reverse_polish
from reverse_polish_notation.calculate import calculate_reverse_polish
from reverse_polish_notation.parser import parse


def main():
    # Инициализация
    defult_value = "(1+2)*4+3"
    if len (sys.argv) < 2:
        print ("Выражение не передано. Расчет будет произведен для тестового выражения: " + defult_value)
        value = defult_value
    else:
        value = sys.argv[1]

    # Парсинг
    lexemes, err = parse(value)
    if err != "":
        sys.exit(1)

    # Преобразования
    reverse_polish, err = to_reverse_polish(lexemes)
    if err != "":
        sys.exit(1)

    # Промежуточный вывод выражение в обратной польской нотации
    print_reverse_polish(reverse_polish)

    # Расчет итогового значения
    result, err = calculate_reverse_polish(reverse_polish)
    if err != "":
        sys.exit(1)

    # Вывод итогового значения
    print(result)


# Вывод выражения
def print_reverse_polish(expression):
    value = ""
    for lex in expression:
        value += " " + lex
    print(value[1:])


if __name__== "__main__":
  main()
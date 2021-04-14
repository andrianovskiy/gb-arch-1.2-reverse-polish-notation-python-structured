from reverse_polish_notation.constants import DELIMS
from reverse_polish_notation.constants import DELIM_FLOAT_POINT

# Преобразование выражаения в набор лексем
def parse(value):
    # Массив с разделителями (операторы и скобки)
    lexemes = []
    num_builder = ""


    if len(value.strip()) == 0:
        err = "Ошибка! Пустая строка"
        print(err)
        return "", err

    # Идем по строке
    for chair in value:
        # Игнорируем пробелы
        if chair != " ":
            # Дошли до разделителя, записываем лексему
            if chair in DELIMS:
                # Записываем лексему в массив
                if num_builder != "":
                    lexemes += [num_builder]
                # Добавляем сам разделитель
                lexemes += [chair]
                num_builder = ""
            elif chair.isdigit() or chair == DELIM_FLOAT_POINT:
                    num_builder += chair
            else:
                err = "Ошибка! Некорректный символ в строке " + chair
                print(err)
                return "", err
    # Обработка конца строки
    if num_builder != "":
        lexemes+=[num_builder]
    
    return lexemes, ""
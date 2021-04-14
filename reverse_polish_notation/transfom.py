from reverse_polish_notation.constants import OPERATORS
from reverse_polish_notation.constants import OPEN_BRACKET
from reverse_polish_notation.constants import CLOSE_BRACKET
from reverse_polish_notation.constants import ADD
from reverse_polish_notation.constants import SUBTRACK
from reverse_polish_notation.constants import MULTIPLY
from reverse_polish_notation.constants import DIVIDE
from reverse_polish_notation.support import isfloat

# Преобразование выражаения в обратну польскую нотацию
def to_reverse_polish(lexemes):
    stack = []
    reverse_polish_lexemes = []
    for lex in lexemes:
        if isfloat(lex):
            reverse_polish_lexemes += [lex]
        elif lex == OPEN_BRACKET:
            stack = [lex] + stack
        elif lex == CLOSE_BRACKET:
            reverse_polish_lexemes, stack, err = push_until_open_bracket(reverse_polish_lexemes, stack, prev_lex)
            if err != "":
                return "", err
        elif stack == []:
                stack = [lex]
        else:
            reverse_polish_lexemes, stack, err = push_until_func(reverse_polish_lexemes, stack, lex, prev_lex)
            if err != "":
                return "", err
        prev_lex = lex

    reverse_polish_lexemes, err = push_stack(reverse_polish_lexemes, stack)
    if err != "":
        return "", err
    return reverse_polish_lexemes, ""

def push_until_func(reverse_polish_lexemes, stack, current_lex, prev_lex):
    if prev_lex in OPERATORS:
        err = "Ошибка! Некорректное выражение"
        print(err)
        return "", "", err
    while(True):
        if stack == [] or stack[0] == OPEN_BRACKET or operator_priority(stack[0]) < operator_priority(current_lex):
            stack = [current_lex] + stack
            break
        if operator_priority(stack[0]) >= operator_priority(current_lex):
            reverse_polish_lexemes += stack[0]
            stack = stack[1:]
    return reverse_polish_lexemes, stack, ""

def push_until_open_bracket(reverse_polish_lexemes, stack, prev_lex):
    if prev_lex in OPERATORS:
        err = "Ошибка! Некорректное выражение"
        print(err)
        return "", "", err
    while(True):
        if (stack == []):
            err = "Ошибка! В выражении либо неверно поставлен разделитель, либо не согласованы скобки"
            print(err)
            return "", "", err
        current_lex = stack[0]
        stack = stack[1:]
        if current_lex == OPEN_BRACKET:
            break
        reverse_polish_lexemes += [current_lex]
    return reverse_polish_lexemes, stack, ""

def push_stack(reverse_polish_lexemes, stack):
    while (stack != []):
        if stack[0] == OPEN_BRACKET:
            err = "Ошибка! В выражении не согласованы скобки"
            print(err)
            return "", err
 
        reverse_polish_lexemes += stack[0]
        stack = stack[1:]
    return reverse_polish_lexemes, ""

# Определение приоритета операции
def operator_priority(operator):
    if operator == ADD or operator == SUBTRACK:
        return 1
    elif operator == MULTIPLY or operator == DIVIDE:
        return 2
    else:
        raise ValueError("Ошибка! Некорректный оператор " + operator)
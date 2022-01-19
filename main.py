CONV_TABLE = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
              (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
              (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def arab_to_roman(number):
    if number <= 0: return ''

    ret = ''
    for arab, roman in CONV_TABLE:
        while number >= arab:
            ret += roman
            number -= arab

    return ret


def roman_to_arab(txt):
    txt = txt.upper()
    ret = 0
    for arab, roman in CONV_TABLE:
        while txt.startswith(roman):
            ret += arab
            txt = txt[len(roman):]
    return ret


def roman(one, two):
    return roman_to_arab(one) + roman_to_arab(two)

ans = roman(input("Введите первое римское число: "), input("Введите второе римское число: "))
print(arab_to_roman(ans))
print(ans)
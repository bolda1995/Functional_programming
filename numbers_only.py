"""В списке digits содержатся строки с числами. Эти строки содержат ошибки: лишние пробелы,
 неправильные разделители целой и десятичной части и тд.
Создайте функцию, которая сначала исправит ошибки в строках,
а затем преобразует каждую строку в вещественное число.
Примените эту функцию ко всем элементам digits с помощью map.
"""

digits = ["12", "145", "  45", "12.4", "45,14", "15 645"]
def tranfer_to_float(digit):
    dig = ""
    for sym in range(len(digit)):
        if digit[0] == "":
            continue
        if digit[sym] == " ":
            continue
        if digit[sym] == ",":
            continue
        if digit[sym - 1] == ",":
            dig += "."
        dig += digit[sym]
    return float(dig)

right_digits = list(map(tranfer_to_float, digits))
print(right_digits)

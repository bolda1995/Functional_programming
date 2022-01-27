"""
Оригинальная map позволяет применять только одну функцию к элементам последовательности.
Однако часто нужно применить сразу несколько map подряд.

Напишите функцию maps, которая может принимать несколько функций. Функции должны применяться к последовательности
в порядке их следования. Последним аргументом должна идти сама последовательность.
"""
def maps(*values):
    new_list = []
    list_val = [*values][-1]
    funcs = [*values][:-1]
    for v in list_val:
        for f in funcs:
            v = f(v)
        new_list.append(v)
    return new_list

def main():
    original_tags = [' python 3', 'SQL', ' PHP ']
    tags = maps(str.strip, str.lower, original_tags)
    print(tags)
if __name__ == "__main__":
    main()

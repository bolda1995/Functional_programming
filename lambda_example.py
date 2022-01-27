from functools import reduce


def main():


    whoami = ['Я', ' ', 'п', 'р', 'о', 'г', 'р', 'а', 'м', 'м', 'и', 'с', 'т']

    whoami = reduce((lambda x, y: str(x) + str(y)), whoami)
    print(whoami)

if __name__ == "__main__":
    main()
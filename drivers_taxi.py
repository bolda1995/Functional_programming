"""
В такси «Везет» есть два условия к водителям при приеме на работу:
    1. Автомобиль кандидата должен быть выпущен не ранее 2008 года (машины 2008 года годятся).
    2. Стаж водителя должен быть не менее трех лет.

В списке drivers содержатся кандидаты в водители,
 используйте функцию filter и lambda-выражение, чтобы убрать неподходящих под
 критерии водителей. Подходящие кандидаты должны быть помещены в переменную taxi_drivers.
"""



def main():
    drivers = [
        {"name": "Семен", "car_year": 2003, "experience": 2},
        {"name": "Степан", "car_year": 2013, "experience": 3},
        {"name": "Ашот", "car_year": 2007, "experience": 5},
        {"name": "Дмитрий", "car_year": 2003, "experience": 0},
        {"name": "Василий", "car_year": 2016, "experience": 1},
        {"name": "Антон", "car_year": 2008, "experience": 7},
        {"name": "Денис", "car_year": 2007, "experience": 5},
        {"name": "Ахмед", "car_year": 2006, "experience": 3},
        {"name": "Виталий", "car_year": 2003, "experience": 2}
    ]
    taxi_drivers = list(filter(lambda driver: driver.get("car_year") >= 2008 and driver.get("experience") >= 3, drivers))
    print(taxi_drivers)
if __name__ == "__main__":
    main()


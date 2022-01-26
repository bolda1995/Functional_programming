def normalize_phone(string):
    phone_number = ""
    for i in string:
        if i.isnumeric():
            phone_number+= i
    return phone_number

phone = normalize_phone("+7 (981) 452-79-72")
print(phone)

def main():
    emails = ["Anton.Ivanov@example.com", "dima@example.com", "Tema.LeveDEV@example.com"]

    lower_emails = list(map(lambda mail: mail.lower(), emails))

    print(lower_emails)


if __name__ == "__main__":
    main()

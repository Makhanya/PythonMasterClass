from csv import writer, DictReader


# def add_user(first, last):
#     with open("CSV/users.csv", "w") as file:
#         csv_writer = writer(file)
#         csv_writer.writerow([first, last])

def add_user(first_name, last_name):
    with open("C:/Users/makhanya/Code/Python/coltsteeleBootcamp/CSV/users.csv", "a") as csvfile:
        csv_writer = writer(csvfile)
        csv_writer.writerow([first_name, last_name])


add_user("Makhanya", "Mzili")


# with open("CSV/users.csv") as file:
#     csv_reader = reader(file)
#     for x in csv_reader:
#         print(x)


def print_users():
    with open("C:/Users/makhanya/Code/Python/coltsteeleBootcamp/CSV/users.csv", "w") as file:
        csv_reader = DictReader(file)
        for row in csv_reader:
            print("{}{}".format(row['First Name'], row['Last Name']))

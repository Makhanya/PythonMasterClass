from csv import reader
def print_users():
    with open("users.csv") as file:
        csv_reader = reader(file)
        users = list(csv_reader)
        for user in users:
            print(user)


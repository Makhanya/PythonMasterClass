from csv import DictReader


def find_user(first_name, last_name):
    with open("CSV/users.csv")as file:
        csv_reader = DictReader(file)
        users = list(csv_reader)
        count = 0
    for x in users:
        count += 1
        if x['First Name'] == first_name and x['Last Name'] == last_name:
            return count
    return "{} {} not found".format(first_name, last_name)


print(find_user("Colt", "Steele"))  # 1
print(find_user("Alan", "Turing"))  # 3
print(find_user("Not", "Here"))  # 'Not Here not found.'

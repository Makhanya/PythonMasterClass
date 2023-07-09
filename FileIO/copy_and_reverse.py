# def copy_and_reverse(file, newFile):
#     f1 = open(newFile, "w")
#     with open(file, "r") as myfile:
#         data = myfile.read()

#     data1 = data[::-1]

#     f1.write(data1)
#     f1.close()
def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])

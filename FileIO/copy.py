import shutil


def copy(file, newFile):
    shutil.copy(file, newFile)


"""
    def copy(file_name, new_file_name):
        with open(file_name)as file:
            text = file.read()

        with open(new_file_name, "w") as new file:
            new_file.write(text)
"""

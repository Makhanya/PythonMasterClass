"""
    Objectives
        *Read text file in Python
        *Write text file in python
        *Use "with":blocks when reading/writing file
        *Describe the different ways to open a file
        *Read CSV files in Python
        *Write CSV files in python

        with Blocks
            Option 1
                file = open("short.txt")
                file.read()
                file.close()

                file.closed #True

            Option 2
                with open("story.txt") as file:
                    data = file.read()
                
                file.closed #True
"""

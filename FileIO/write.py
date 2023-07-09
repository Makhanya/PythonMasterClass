"""
    Writing Files
        *You can also use open to write to a file
        *Need to specify the "w" flag as the second argument
        """

# Writing File Example
# with open("haiku.txt", "w")as file:
#     file.write("Writing files is great\n")
#     file.write("Here's another line of text\n")
#     file.write("Closing now, goodbye!")

# with open("FileIO/haiku.txt", "w") as file:
#     file.write("Here's one more haiku\n")
#     file.write("What about the older one\n")
#     file.write("Let's go check it out")

with open("FileIO/lol.txt", "w") as file:
    file.write("haha"*1000)

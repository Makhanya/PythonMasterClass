def statistics(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()

    return {
        "lines": len(lines),
        "words": sum(len(line.split(" "))for line in lines),
        "characters": sum(len(line)for line in lines)
    }

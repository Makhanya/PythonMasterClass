"""
    Writing CSV files
        Using Dictionaries
            *DicWriter - creates a writer object for writing using Dictionaries
            *fieldnames - kwargs for the DictWwriter specifying headers
            *writeheader - method on a writer to write head row
            *writerow - method on a writer to write a row based on a dicitionary
            
            """
from csv import DictWriter
with open("CSV/example.csv", "w") as file:
    headers = ["Character", "Move", "Speed"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Character": "Ryu",
        "Move": "Hadouken",
        "Speed": "5km"
    })

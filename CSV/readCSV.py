"""
    Reading CSV Files
        *CSV files are common file format for tabular data
        *We can read CSV files just like other text files
        *Python has a built-in CSV module to read/write CSVs more easily 

       
       Using Reader
            # from csv import reader
            # with open("fighters.csv")as file:
            #     csv_reader = reader(file)
            #     next(csv_reader)
            #     for fighter in csv_reader:
            #         print(f"{fighter[0]} is from {fighter[1]}")
            #      #   print(row)
            # from csv import reader
            # with open("fighters.csv") as file:
            #     csv_reader = reader(file)
            #     data = list(csv_reader)
            #     print(data)

        Using DictReader

"""
from csv import DictReader
with open("fighters.csv")as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # each row is an OrderedDict!
        print(row)

""" Other Delimiters
        Readers accept a delimiter kwarg in case you data is'nt separated by commas
        
            from csv import reader
            with open("example.csv") as file:
                    csv_reader = reader(file,delimiter="|")
                    for row in csv_reader:
                        #each row is a list!
                        print(row)"""

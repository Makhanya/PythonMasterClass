"""
    Writing to CSV files
        Using Lists
            *writer - create a writer object for writing to CSV
            *writerrow - method on a writing a row to the CSV
            
             """

from csv import writer
with open("cats.csv", "w")as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Blue", 4])
    csv_writer.writerow(["Kitty", 2])

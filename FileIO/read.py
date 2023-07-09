""" 
    Reading files
        *You can read a file with open function
        *open returns a file object to you
        *You can read a file object with the read method
        
        File Read Example
            file = open("~/short.txt")
            file.read()
            print(file)

            file.readline() #reads the whole line
            

        """


""" Cursor Movement

        *Python reads files by using a cursor
        *This is like the cursor you see when your're typing
        *After a file is read, the cursor is at the end of the file

            file.seek(0) #moves the cursor to the beginning of the line

        
    Closing a file
        *You can close a file with the close method
        *You can check if a file is closed with the closed attribute
        *Once closed, a file can't be read again
        
        
        """
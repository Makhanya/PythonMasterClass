"""
    ___name___
        *When run, every python file has a ___name___ varuable
        *If the file is the main file being run, its value is "__main__" 
        *Otherwise, its value is the file name
        
    import revisited
        When you use import Python...
        
            1.Tries to find the module(if it fails, it throws an error),
            2.Runs the code inside of the module being imported,

    ignoring Code on import
        if __name__ == "__main__":
            #this code will only run
            #if the file is the main file!
            """

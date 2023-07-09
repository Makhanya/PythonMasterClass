"""Handling Errors
       In Python, it is strongly encouraged to use try/except blocks,
       to catch exceptions when we can do something about them. 
       let see what that looks like 
       
       foobar = False
try:
    foobar
except:
    print("Problem!")
print("After the try")
       """

""" Why Not Catch them all
        try:
            colt
        except:
            print('you tried to use a variable that was never declared!
            
        what we are doing here is catching every error,which means we are not able to correctly identify
        'what' went wrong. It is highly discouraged to do this
    Any Better
        try:
            colt
        except:
            print('you tried to use a variable that was never declared!)    
        
        """


# def get(d, key):
#     try:
#         return d[key]
#     except KeyError:
#         return None


# d = {"name": "Ricky"}
# print(get(d, "name"))

# try
# except
# else
# finally
try:
    num = int(input("Please enter a number: "))
except:
    print("Thats not a number!")
else:
    print("Good job, you entered a number!")
    #break
finally:
    print("Im in the end 'Finaly'")

"""

     Assertions
        *We can make simple assertions with the assert keyword
        *assert accepts ans expression
        *Returns None if teh expression is truthy
        *Raises an AssertionError if the expression is falsy
        *Accepts an optional error message as a second argument

        Example
            def add_positive_numbers(x,y):
                assert x>0 and y>0,"Both numbers must be positive!"
                return x + y

            print(add_positive_numbers(1,1))
            print(add_positive_numbers(1,-1))


            def eat_junk(food):
                assert food in [
                    "pizza",
                    "ice cream",
                    "candy",
                    "fried butter"
                ], "Food must be a junk food"
            return f"NOM NOM NOM I am eating {food}"
food = input("Enter a food please: ")
print(eat_junk(food))

                Assertions Warning
                    If a Python file is run with the -O flag,
                    assertions will not be evaluated

                        #Don't write code like this!
                        def do_something_bad(user):
                            assert user.is_admin, "Only admins can do bad things!"
                            destroy_a_bunch_of_stuff()
                            return "MUA HA HA HA!"

"""

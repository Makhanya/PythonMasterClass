"""

    RegEx
        Regular Expression
            what are regular expressions
                *A way of describing patterns within search strings

        Validating email
            name.surname@gmail.com
                starts with 1 or more letter, number, +, _,. then
                a single @ sign then
                1 or more letter, number, or- then a single dot then
                ends with 1 or more letter, number,-,or .
                    lets use a regular expression!
                        (^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)

        Potential Use Cases
            *Credit card number validating
            *Phone number validating
            *Advanced find/replace in text
            *Formatting text/output
            *Syntax highlighting


"""


def hello_world(thingy):
    # I do nothing
    print("Hello World!")

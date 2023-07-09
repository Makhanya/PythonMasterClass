import re


def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    else:
        return None


def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input)


#
# print(extract_all_phones("my phone is 456 567-6787 or call me at 435 666-4324"))
#

#
#
# print(extract_phone("my phone is 456 567-6787"))
# print(extract_phone("my number is 432 567-8976222"))
# print(extract_phone("432 567-8976"))
# print(extract_phone("432 567-8976 is the phone number"))

def is_valid_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False


# def is_valid_phone(input):
#     phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
#     match = phone_regex.search(input)
#     if match:
#         return True
#     return False


print(is_valid_phone("423 456-8970"))
print(is_valid_phone("432 734-8976 ads"))
print(is_valid_phone("ads 432 567-7869 d"))

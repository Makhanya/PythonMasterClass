"""
    Using REGEX with Python
"""
import re

pattern = re.compile(r'\d{3} \d{3}-\d{4}')

res = pattern.search('Call me at 415 555-4242!')

print(res.group())

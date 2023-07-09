"""

"""
import re

text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

# pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z]) [a-z]+', re.I)
pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z]) [a-z]+', re.IGNORECASE)
result = pattern.sub("\g<1> \g<2>", text)
print(result)

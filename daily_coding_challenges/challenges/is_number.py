import re
from typing import List

def is_number(number: str) -> bool:
    number_regex = re.compile(r'\d+')


number_regex = re.compile(r'\d+')

outcome: bool = isinstance(number_regex, re.RegexFlag)
print(dir(re))
print(outcome)
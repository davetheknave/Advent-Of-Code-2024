import re

def regex(pattern: str, subject: str):
    matches = re.match(pattern, subject)
    return matches.groups() if matches is not None else None

def regexAll(pattern: str, subject: str):
    matches = re.finditer(pattern, subject)
    return matches

def word_to_digit(word: str) -> str:
    dat = {"one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9}
    if word in dat:
        return str(dat[word])
    else:
        return word
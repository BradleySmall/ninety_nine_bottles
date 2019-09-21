#!/usr/bin/python
"""
Program to generate the song Ninety-nine Bottles of Beer
"""


def num2name(num):
    """
    function that takes a number and returns the text name
    this will only work for 0 - 99
    it provides no error handling and assumes that a valid number will be
    passed in
    """
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
            "eighty", "ninety"]
    ones = ["", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]

    ten = num // 10
    one = num % 10

    # 99-20
    if ten > 1:
        if one == 0:
            name = tens[ten]
        else:
            name = tens[ten] + "-" + ones[one]

    # 19-10
    if ten == 1:
        name = teens[one]

    # 9-0
    if ten == 0:
        if one == 0:
            name = "No"
        else:
            name = ones[one]

    return name


def count2s(num):
    """
    Returns an "s" for any number other than 1
    """
    if num == 1:
        return ""

    return "s"


def main():
    """
    Main driver loop. Maintains the base text and substitutes the numbers
    to make it work. Checks for count to compensate for bottle vs bottles,
    in 2 places. Calculate the plurality and have one output string set
    """

    for count in range(99, 0, -1):
        values = (num2name(count).capitalize(), count2s(count),
                  num2name(count).capitalize(), count2s(count),
                  num2name(count-1).capitalize(), count2s(count-1))
        print("%s bottle%s of beer on the wall.\n"
              "%s bottle%s of beer. Take one down,\n"
              "pass it around... %s bottle%s of beer.\n" % values)


if __name__ == "__main__":
    main()

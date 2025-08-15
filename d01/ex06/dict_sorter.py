
"""
Algorithm flow:

1. Bind transformed dictionary variable list_of_tuples into country_dict.
2. Pass country_dict to function format_dict.
3. format_dict function returns a dict
 where the key is value (transformed to int) and value is key,
 and sorted in decending order based on the value-int.
4. formatted_print function print the country name
 using the sorted dictionary argument.
If the value is list, then sort the value in alphabetical order and print.

**justification for switching and making the num int: To make the sorting easy.
"""


def formatted_print(country_dict: dict) -> None:
    """
    Prints the country names in descending order
    by number, then alphabetical order by name if the numbers are equal
    """

    for value in country_dict.values():
        if isinstance(value, list):
            sorted_value = sorted(value)
            for item in sorted_value:
                print(item)
        else:
            print(value)


def format_dict(dict_list: dict) -> dict:
    """
    Returns a reverse sorted dict
    where number is the key as an
    int type and the country is the value
    """

    fmt_dict: dict = {}

    for key, value in dict_list.items():
        if not value or not value.isdigit():
            continue
        value_int = int(value)
        if value_int not in fmt_dict:
            fmt_dict[value_int] = key
        else:
            if isinstance(fmt_dict[value_int], list):
                fmt_dict[value_int].append(key)
            else:
                fmt_dict[value_int] = [fmt_dict[value_int], key]
    return dict(sorted(fmt_dict.items(), reverse=True))


def main():

    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]

    country_dict = dict(list_of_tuples)
    formatted_dict = format_dict(country_dict)
    formatted_print(formatted_dict)


if __name__ == "__main__":
    main()

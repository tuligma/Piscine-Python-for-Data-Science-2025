

def formatted_print(dict_list: dict, fmt_dict: dict) -> None:
    """
    Print fmt_dict with precise formatting
    using dict_list sequece
    """

    for country, num in dict_list.items():

        if isinstance(fmt_dict[num], list):
            for value in fmt_dict[num]:
                if value == country:
                    print(f"'{num}' : '{value}'")
        elif fmt_dict[num] == country:
            print(f"'{num}' : '{fmt_dict[num]}'")


def format_dict(dict_list: dict) -> dict:
    """
    Returns a dict where number is the key and the country is the value
    """

    fmt_dict: dict = {}

    for key, value in dict_list.items():
        if value not in fmt_dict:
            fmt_dict[value] = key
        else:
            fmt_dict[value] = [fmt_dict[value], key]

    return fmt_dict


def main():
    """
    Calls formatted_print and pass the argument dict_list
    and function format_dict that
    returns modified swicth key/values of dict_list.
    """

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

    dict_list = dict(list_of_tuples)
    formatted_print(dict_list, format_dict(dict_list))


if __name__ == "__main__":
    main()

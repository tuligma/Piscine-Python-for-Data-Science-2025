

def data_types() -> None:
    a, b, c, d, e, f, g, h = 1, "One", 1.0, True, [], {}, (), set([])

    lst = [a, b, c, d, e, f, g, h]

    types = ""
    for x, item in enumerate(lst):
        types += type(item).__name__.strip("'")
        if x is not len(lst) - 1:
            types += ", "

    print(f"[{types}]")


if __name__ == "__main__":
    data_types()

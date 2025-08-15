
def start(item: str) -> bool:
    return item.startswith('"') and not item.endswith('"')


def mid(item: str) -> bool:
    return (
        item not in ("false", "true")
        and not item.startswith('"')
        and not item.endswith('"')
    )


def end(item: str) -> bool:
    return not item.startswith('"') and item.endswith('"')


def checker(item: str) -> int:
    if item in ("false", "true"):
        return True
    elif start(item) or mid(item) or end(item):
        return False
    else:
        return True


def slice_get(lst: list) -> list:
    return [item for item in lst if not checker(item)]


def pop_insert(lst: list, to_pop: list, i: int) -> list:
    for item in to_pop:
        lst.remove(item)
    lst.insert(i, ",".join(to_pop))
    return lst


def change_fix(items: list) -> list:
    final = []
    for item in items:
        line = item.split(",")
        if len(line) > 6 and slice_get(line):
            to_pop = slice_get(line)
            i_tp = line.index(to_pop[0])
            line = pop_insert(line, to_pop, i_tp)
        line = "\t".join(line)
        final.append(line)
    return final


def read_write(content: str) -> str:
    items = content.splitlines()
    final = change_fix(items)
    return "\n".join(final)


def main():
    path = "ds.csv"
    outfile = "ds.tsv"
    with open(path, "r") as f:
        content: str = f.read()
    try:
        assert content, "File is empty"
        out = read_write(content)
        with open(outfile, "x") as o_f:
            o_f.write(out)
    except AssertionError as e:
        print(f"Assertion Error: {e}")


if __name__ == "__main__":
    main()

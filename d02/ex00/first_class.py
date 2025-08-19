class Must_read:
    """
    Read and prints 'data.csv' file content.
    If file does not exist and the
    file is empty, it raises an
    exception.
    """

    path = "data.csv"

    try:
        with open(path, "r") as f:
            data = f.read()

        if not data:
            raise ValueError("The file is empty.")

        print(data)
    except FileNotFoundError:
        print(f"FileNotFoundError: No such file or directory: {path}")
    except ValueError as e:
        print(f"ValueError: {e}")


if __name__ == "__main__":
    pass

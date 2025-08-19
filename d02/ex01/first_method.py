class Research:
    """
    ->  The class method 'file_reader()' reads
        and returns 'data.csv' file content.

    ->  If file does not exist or the file is empty,
        it raises FileNotFoundError and ValueError
        exception.
    """

    @staticmethod
    def file_reader():
        path = "data.csv"

        try:
            with open(path, "r") as f:
                data = f.read()

            if not data:
                raise ValueError("The file is empty.")

            return data.strip()
        except FileNotFoundError:
            raise FileNotFoundError(f"No such file or directory: {path}")
        except ValueError as e:
            raise ValueError(e)


if __name__ == "__main__":
    """
    ->  Use try-except to print the return value
        of the class Research's
        class method 'file_reader()'.

    ->  It prints error message,
        if it raises FileNotFoundError
        and ValueError exceptions.
    """

    try:
        print(Research.file_reader())
    except (FileNotFoundError, ValueError) as e:
        print(f"{type(e).__name__}: {e}")

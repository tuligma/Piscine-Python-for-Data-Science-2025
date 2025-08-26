from random import randint


class Research:
    """
    Research class for handling file input, reading,
    validation and returning its content.

    Overview:
        -> Initialize with a file path
           using '__init__' constructor

        -> Returns the file's content by reading
           and validating it through
           'file_reader() method'.

        -> Returns a the list of the body content
           of the file, It validates the structure
           of the content.

    Parts:
    __init__: (constructor)
        -> Stores the given path string as 'self.path'

    file_reader():
        -> Reads, validate and returns the content of the file at 'self.path'
           It takes has_header defaults into True as an additional argument.
        -> Raises:
            -> FileNotFoundError, PermissionError, IOError, UnicodeDecodeError
               if the file cannot be opened.
            -> ValueError if the content is empty
            -> ValueError if the content does not follow the expected format.
               (checked by '_validate_data()')
            -> ValueError if the 'has_header's value does not align with
               the contents of the file.

    _validate_data():
        -> Validates file structure and
           returns the list content's body

        -> Expected format:
            - one or more line after header
              that either contain 0 or 1,
               and never both of them delimited by comma.
    """

    def __init__(self, path):
        """
        Stores the given path string as 'self.path'
        """
        self.path = path

    def _validate_data(self, data_lines) -> list:
        """
        -> Validates file structure and
           returns the list content's body

        -> Expected format:
            - one or more line after header
                that either contain 0 or 1,
                and never both of them delimited by comma.

        Edge Cases:
            Iterating on content list.
            -> If the list's items in content does not have a length of 2.
            -> If the list of values within content list are empty.

            Check values:
            -> If the values are not intances of ([0, 1], [1, 0]).
        """
        ERR_CTR = f"Cannot read the file {self.path}."
        lines = []
        for x, items in enumerate(data_lines):
            line = items.strip().split(",")
            if len(line) != 2 or not all(v.strip() for v in line):
                raise ValueError(f"_validate_data(): {ERR_CTR} -> line:{line}")

            try:
                value = [int(v.strip()) for v in line]
                if value not in ([0, 1], [1, 0]):
                    raise ValueError
                lines.append(value)
            except ValueError:
                raise ValueError(f"_validate_data(): {ERR_CTR} -> line:{line}")
        return lines

    def file_reader(self, has_header=True) -> list:
        """
        Reads, validates and returns the content body
        of the file at 'self.path' as a list.

        It takes 'has_header' defaults to True
        as an additional argument, It verifies
        has_header's value if it aligns on the file,
        if not it raises ValueError.

        -> Raises:
            -> FileNotFoundError, PermissionError, IOError, UnicodeDecodeError
               if the file cannot be opened.
            -> ValueError if the content is empty
            -> ValueError if the content does not follow the expected format.
               (checked by '_validate_data()')
            -> ValueError if the 'has_header's value does not align with
               the contents of the file and expected format.

        Edge: Cases
            Opening the file:
            -> if file related error upon opening.
                - Permission
                - Not Found
                - I/O
                - Mismatch encoding

            File Content:
            -> if the content of the file is empty.
            -> if the content has lessthan 2 length.

            File header:
            -> if has_header is true but header on file is missing
            -> if has_header is false but header on file exist
            -> if '_validate_data' raises an error.
        """
        ERR_NOF = f"No such file or directory: {self.path}"
        ERR_CTR = f"Cannot read the file {self.path}."
        ERR_PRM = f"You have no permision to access {self.path}"
        ERR_HRE = f"has_header is {has_header}, but contradicts on {self.path}"

        try:

            with open(self.path, "r") as f:
                data_lines = f.readlines()
            if not data_lines or len(data_lines) < 2:
                raise ValueError(ERR_CTR)

            header = [item.strip() for item in data_lines[0].split(",")]
            if len(header) != 2 or not all(v.strip() for v in header):
                raise ValueError(ERR_CTR)

            body_pattern = (["0", "1"], ["1", "0"])
            if (
                has_header
                and header in body_pattern
                or not has_header
                and header not in body_pattern
            ):
                raise ValueError(ERR_HRE)
            elif has_header and header[0] == header[1]:
                raise ValueError(ERR_CTR)

            body = data_lines[1:]
            if not has_header:
                body = data_lines
            return self._validate_data(body)
        except FileNotFoundError:
            raise FileNotFoundError(f"file_reader(): {ERR_NOF}")
        except PermissionError:
            raise PermissionError(f"file_reader(): {ERR_PRM}")
        except IOError as e:
            raise IOError(f"file_reader(): {e}")
        except UnicodeDecodeError as e:
            raise UnicodeDecodeError(f"file_reader(): {e}")
        except (IOError, UnicodeDecodeError, ValueError) as e:
            raise ValueError(f"file_reader(): {e}")

    class Calculations:
        """
        nested Calculation class of Research Class,
        It counts the head and tails of the data from
        'file_read()' and its fraction percentage.
        """

        def __init__(self, lines):
            """
            Stores the given lines list to 'self.lines'
            """
            self.lines = lines

        def counts(self):
            """
            Returns a string of head and tail counts and
            store it in self.ht_counts as a list.
            Takes self.lines as an argument and validates
            its expected structure.

            Raises:
                -> TypeError if the values are not int.
                -> ValueError if the length is not 2.
                -> ValueError if the values are neither 1 or 0.

            Edge Cases:
                Argument check:
                -> if the passed argument is empty

                Iterate on the list:
                -> if each items on the list has a length of 2
                -> if each values on the items are not int
                -> if each values on the items are either 0 or 1.
            """
            try:
                if not self.lines:
                    raise ValueError("List is empty.")

                for item in self.lines:
                    if len(item) != 2:
                        raise ValueError(f"Invalid stucture: length: {item}")
                    elif not all(isinstance(v, int) for v in item):
                        raise TypeError(
                            f"Invalid type: got {item}"
                            f"{[type(v) for v in item]}"
                        )
                    elif not all(v in (1, 0) for v in item):
                        raise ValueError(f"Invalid value/s: {item}")
                ht_counts = [0, 0]
                for item in self.lines:
                    if item[0] == 1:
                        ht_counts[0] += 1
                    elif item[1] == 1:
                        ht_counts[1] += 1
                self.ht_counts = ht_counts
                return ht_counts

            except TypeError as e:
                raise TypeError(f"counts() -> {e}")
            except ValueError as e:
                raise ValueError(f"counts() -> {e}")

        def fractions(self):
            """
            Returns a string of fractions and store it in
            self.ht_fractions as a list.
            Takes 'ht_counts' as an arguments and
            validates its expected structure an values.

            Raises:
                -> TypeError if the converted value is not digit.
                -> ValueError if length is not 2.
                -> ValueError if the values are not digits.

            Edge Cases:
                Argument check:
                -> if the items in converted argument
                   to list has a length of 2.
                -> if each items values are digits.

                Zero Division:
                -> if the total of collated counts are zero.
            """
            try:
                if len(self.ht_counts) != 2 or not all(
                    isinstance(v, int) for v in self.ht_counts
                ):
                    raise ValueError(f"Invalid counts: {self.ht_counts} ")

                counts = [int(n) for n in self.ht_counts]
                total = sum(n for n in counts)
                if total == 0:
                    return "0.0 0.0"
                head = (counts[0] / total) * 100
                tail = (counts[1] / total) * 100
                self.ht_fractions = [head, tail]
                return [head, tail]
            except TypeError as e:
                raise TypeError(f"fractions(): {e}")
            except ValueError as e:
                raise ValueError(f"fractions(): {e}")


class Analytics(Research.Calculations):
    """
    Analytics class is a child class of nested Calculation class
    of Research class. It show a list of list of predictions based
    on the number given and it shows the last item on the data from
    'file_read()' method of Research Class.
    """

    def __init__(self, lines):
        super().__init__(lines)

    def predict_random(self, num):
        """
        Returns a list of list prediction randomly
        based on the value of the argument.

        Raises:
            -> ValueError if argument is not integer.
            -> ValueError if the integer is less than 1.

        Edge cases:
            Argument check:
            -> if the argument is not integer
            -> if the argument's value is less than 1


        """
        if not isinstance(num, int):
            raise TypeError(
                f"Analytics: predict_random(): "
                f"Should be int, got {type(num).__name__}."
            )
        elif num < 1:
            raise ValueError(
                f"Analytics:predict_random(): "
                f"Should be greater than 1, got {num}."
            )
        return [[1, 0] if randint(0, 1) == 1 else [0, 1] for _ in range(num)]

    def predict_last(self):
        """
        Returns the last item of the data from 'file_reader()'
        that is stored from 'self.lines'

        Raises:
            -> ValueError if 'self.lines' is empty or the last item is empty.
            -> ValueError if the last item length is not 2 and all the values
               in the items are not integer.

        Edgecases:
            Argument check:
            -> if the list is empty
               and if the last item of the list is empty.
            -> if the last item's length is not two
               and each value is not an integer.
        """
        if not self.lines or not self.lines[-1]:
            raise ValueError("Analytics:predict_last(): The list is empty.")
        elif len(self.lines[-1]) != 2 or not all(
            isinstance(v, int) for v in self.lines[-1]
        ):
            raise ValueError(
                f"Analytics:predict_last(): Invalid structure {self.lines[-1]}"
            )
        return self.lines[-1]

    @staticmethod
    def save_file(data, filename, ext='txt'):
        """
        Save the report into a txt file.

        Raises:
            -> IOError if any error using open().
        """
        try:
            with open(f"{filename}.{ext}", "w") as report:
                report.write(data)
        except IOError as e:
            raise IOError(f"Analytics: save_file(): {e}")

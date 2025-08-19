import sys
import os


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

        -> Validates the file structure with
           '_err_handler()' private method

    Parts:
    __init__: (constructor)
        -> Stores the given path string as 'self.path'

    file_reader():
        -> Reads, validate and returns the content of the file at 'self.path'.
        -> Raises:
            -> FileNotFoundError, PermissionError, IOError, UnicodeDecodeError
               if the file cannot be opened.
            -> ValueError if the content is empty
            -> ValueError if the content does not follow the expected format.
               (checked by '_err_handler()')

    _err_handler():
        -> Validates file structure

        -> Expected format:
            - a header with two strings delimited by comma.
            - one or more line after header
                that either contain 0 or 1,
                and never both of them delimited by comma.
    """

    def __init__(self, path):
        """
        Stores the given path string as 'self.path'
        """
        self.path = path

    def _err_handler(self, data) -> bool:
        """
        -> Validates file structure

        -> Expected format:
            - a header with two strings delimited by comma.
            - one or more line after header
                that either contain 0 or 1,
                and never both of them delimited by comma.
        """

        try:
            data_check = data.split("\n")
            if len(data_check) < 2:
                raise ValueError

            for x, item in enumerate(data_check):

                line = item.split(",")
                if len(line) != 2 or not all(v.strip() for v in line):
                    raise ValueError

                if x == 0:
                    if line[0] == line[1]:
                        raise ValueError
                else:
                    if not (line == ['0', '1'] or line == ['1', '0']):
                        raise ValueError
            return True
        except ValueError:
            return False
        

    def file_reader(self) -> str:
        """
        Reads, validates and returns the content of the file at 'self.path'.
        -> Raises:
            -> FileNotFoundError, PermissionError, IOError, UnicodeDecodeError
               if the file cannot be opened.
            -> ValueError if the content is empty
            -> ValueError if the content does not follow the expected format.
               (checked by '_err_handler()')
        """
        ERR_NOF = f"No such file or directory: {self.path}"
        ERR_EMT = f"{self.path} is empty"
        ERR_CTR = f"Cannot read the file {self.path}."
        ERR_PRM = f"You have no permision to access {self.path}"

        try:

            with open(self.path, "r") as f:
                data = f.read()
            if not data:
                raise ValueError(ERR_EMT)

            if not self._err_handler(data):
                raise ValueError(ERR_CTR)

            return data.strip()
        except FileNotFoundError:
            raise FileNotFoundError(ERR_NOF)
        except PermissionError:
            raise PermissionError(ERR_PRM)
        except (IOError, UnicodeDecodeError, ValueError) as e:
            raise ValueError(e)


if __name__ == "__main__":
    """
    ->  Validates the arguments
        and the file if it exist

    ->  Create an instance of Reseacrch
        and prints the content of the
        file.

    ->  If it encounter an error,
        it prints the error message
    """

    try:

        if len(sys.argv) != 2:
            raise ValueError(
                "Usage: python3 first_constructor <path to file e.g data.csv>"
            )
        elif not os.path.isfile(sys.argv[1]):
            raise FileNotFoundError(f"No such file or directory: {sys.argv[1]}")

        content = Research(sys.argv[1])
        print(content.file_reader())
    except (FileNotFoundError, ValueError, PermissionError) as e:
        print(f"{type(e).__name__}: {e}")

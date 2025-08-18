import sys


def email_filter(email: str) -> bool:
    """
    Returns
    True, if the below conditions met.
    1. if the email ends with '@corp.com'
    2. if there is 1 '.' before '@corp.com'
    3. if '.' is not the first element or before '@corp.com'
    False, if not
    """

    return (
        email.endswith("@corp.com")
        and email[:-9].count(".") == 1
        and "." not in (email[0], email[-10])
    )


def letter_starter(email: str) -> str:
    """
    It takes an email and extract the name from the
    file 'employees.tsv'.
    Returns the first paragraph of the letter
    with the extracted name.

    Flow:
        -> make the argument lowercase and strip
           whitespaces and bind to variable 'e_mail'.

        -> asses the 'e_mail' if is not valid.
           if not valid it raises ValueError
           and returns an error message

        -> Open and read the file. Bind the
           content to variable 'employees'.
           if the file does not exist,
           it will raise FileNotFoundError
           and returns an error message

        -> make the a 2d list using list
           comprehension.
           It iterates through splitted employees
           and each items will be splitted as well,
           while ommiting the header list.
           It will be bind to 'employees_list'.

        -> Iterate through employees_list.
           If the length of employee is more than 'EMAIL'(2)
           and If the value of employee on the index 'EMAIL'(2)
           is equal to the value of the e_mail.

        -> It returns first paragraph of letter using
           f-string, including the variables 'name'
           and 'LETTER'

        -> If the loop is finished and did not find
           a match. It raises a ValueError
           and returns error message.
    """

    ERR_NOF = "FileNotFoundError: No such file or directory:"
    ERR_IEA = f"Invalid email address: {email}"
    ERR_ENF = f"{email} email not found!"
    LETTER = (
        "welcome to our team. We are sure that it will be"
        " a pleasure to work with you. That's a precondition"
        " for the professionals that our company hires."
    )

    NAME = 0
    EMAIL = 2
    path = "employees.tsv"

    try:

        e_mail = email.lower().strip()
        if not email_filter(e_mail):
            raise ValueError(ERR_IEA)

        with open(path, "r") as file:
            employees = file.read()

        employees_list = [
            item.split()
            for x, item in enumerate(employees.split("\n"))
            if x > 0 and item
        ]

        for employee in employees_list:
            if len(employee) > EMAIL and employee[EMAIL] == e_mail:
                return f"Dear {employee[NAME]}, {LETTER}"

        raise ValueError(ERR_ENF)

    except FileNotFoundError:
        return f"{ERR_NOF} {path}"
    except ValueError as e:
        return f"ValueError: {e}"


def main():
    """
    Entry point of the program.

    Flow:
        -> It asseses the number of arguments
           If its not equal to two.
           It prints the error message
           and exit the program using
           sys.exit

        -> prints the return value of
           the function 'letter_starter' with
           argument index 1.
    """
    ERR_ARG = "Usage: python3 names_extractor.py <name.lastname@corp.com>"
    if len(sys.argv) != 2:
        print(ERR_ARG)
        sys.exit(0)
    print(letter_starter(sys.argv[1]))


if __name__ == "__main__":
    main()

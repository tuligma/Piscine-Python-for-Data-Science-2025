import sys


"""
Edge cases:

1. If no arguments given and file doesnt exist
2. emails has duplicates
3. malformed emails.
    -> no @corp.com
    -> no first_name
    -> no last_name
    -> no separator
Situations:
if no @corp.com but @something.com -> dont accept
if no @corp.com but name.lastname? -> dont accept - probably typo error.
if no firstname but . is existing? accept or no? dont accept
if no lastname but . is existing? accept or no? dont accept
if no firstname or last name without . existing? dont accept.

Sample file content:
ivan.petrov@corp.com
emma.geller@corp.com
john.smith@corp.com
john.smith@corp.com
banjo.@corp.com
.pentinio@corp.com
pentinio@corp.com
zach.Banjo@facebook.com
emma.geller@corps.com
"""


def email_filter(email: str) -> bool:
    """
    Returns True or False
    if the below conditions met.
    1. if the email ends with '@corp.com'
    2. if there is 1 '.' before '@corp.com'
    3. if '.' is not the first element or before '@corp.com'
    """

    return (
        email.endswith("@corp.com")
        and email[:-9].count(".") == 1
        and "." not in (email[0], email[-10])
    )


def names_extractor(path: str) -> None:
    """
    Creates a table with the name, lastname and email extracted
    from emails list and store in a "employees.tsv" file.

    Flow:
        -> If file dont exist it raises FileNotFoundError

        -> Open the file, read and bind to variable 'emails'.

        -> If the 'email' is empty. It raises ValueError,
           and prints error message

        -> Split the emails with the delimeter '\n.
           use set() to remove the duplicate emails
           and transform into a list, and bind to variable email_lst

        -> Iterates trough email_lst
        -> Each emails will be asses using email_filter if it is a valid
           email or not.
        -> If the email is valid:
            -> it extract the name and last name, by spliting the email
               using the delimiter '.' only up until before '@corp.com'.
            -> it will loop to the extracted name and last name to make
               it lowercase and Capitalize.
            -> the list will be bind to employee variable.
            -> Adds the email to the employee variable by appending.
            -> make the list into string using join()
               with the delimiter '\t' and add '\n' in the end,
               and it will be appended to the variable body.
        -> If the email is not valid:
            -> Do nothing and move to the next email.

        -> Open the file 'employees.tsv with mode 'w+' and write
           the 'HEADER' and 'body' variable.
    """

    ERR_NOF = "FileNotFoundError: No such file or directory:"
    ERR_EMT = f"{path} file is empty."
    HEADER = "Name\tSurname\tEmail"

    try:

        with open(path.strip(), "r") as file:
            emails = file.read()

        if not emails:
            raise ValueError(ERR_EMT)

        emails_lst = list(set(emails.split("\n")))
        body = ""

        for email in emails_lst:

            if email_filter(email):
                employee = [
                    item.lower().capitalize()
                    for item in email[:-9].split(".")
                    ]
                employee.append(email)
                body += "\n" + "\t".join(employee)

        with open("employees.tsv", "w") as out_file:
            out_file.write(HEADER + body)

        # print("employees.tsv has been generated.")
    except FileNotFoundError:
        print(f"{ERR_NOF} {sys.argv[1]}")
    except ValueError as e:
        print(f"ValueError: {e}")


def main():
    """
    Entry point to the program.

    Flow:
        -> It asseses the number of arguments
            If its not equal to two.
            It prints the error message
            and exit the program using
            sys.exit

        -> Calls the names_extractor function
           to generate the "employees.tsv" file.
           Which contains of employee details
           such as Name, Lastname and email.
    """
    ERR_ARG = "Usage: python3 names_extractor.py <path to work emails file>"
    if len(sys.argv) != 2:
        print(ERR_ARG)
        sys.exit(0)
    names_extractor(sys.argv[1])


if __name__ == "__main__":
    main()

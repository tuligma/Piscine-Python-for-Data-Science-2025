import sys

"""
Instruction:
Exercise 07
Sets
Turn-in directory : ex07/
Files to turn in : marketing.py
Allowed functions : import sys
    In this exercise, imagine that you work in a marketing department. You will operate
    with different lists of email accounts. The first list is your clients’ email accounts. The
    second list contains the email accounts of the participants in your most recent event
    (some of them were your clients). The third list contains the accounts of your clients who
    viewed your most recent promotional email.
    In business terms, you need to:
    • Create a list of those who have not seen your promotional email yet. The list will
    be sent to the call center to reach those people.
    • Create a list of the participants who are not your clients. You will send them an
    introductory email about your products.
    • Create a list of the clients who did not participate in the event. You will send them
    a link to the video and slides of the event.
    Technical details:
    • Create different functions that convert your lists to sets and use the set operators
    that you need to use to perform the aforementioned business tasks and return the
    required lists of email accounts.
    • Arrange your code in a script. The script takes the name of the task to perform as
    an argument: call_center, potential_clients, loyalty_program. If the wrong name
    is given, raise an exception.
    • For this exercise you need to use the following three lists:
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill\
    _gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', '
    elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
"""

"""
Legend:
'clients':
    -> All of the existing clients emails

'participants':
    -> Participated in the recent events
    -> Some are clients and some are not

'recipients':
    -> existing clients who viewed most recent promotional email

Task:
'call_center':
 - list not seen your promotional email yet:
    -> returns a list of remaining emails
       from combined sets of clients and participants
       that did not seen promotional email yet (recipients set).

'potential_clients':
 - list of the participants who are not your clients
    -> returns a list of remaining emails from participants set
       that are not existing clients (client set)

loyalty_program':
 - list of the clients who did not participate in the event.
    -> returns a list of remaining emails
       from clients set that did not
       participated in the event (participants set)
"""


def automate_task(
        task: str,
        c_list: list,
        p_list: list,
        r_list: list
) -> list:
    """
    Legend:
    'clients':
        -> All of the existing clients emails

    'participants':
        -> Participated in the recent events
        -> Some are clients and some are not

    'recipients':
        -> existing clients who viewed most recent promotional email

    Task:
    'call_center':
    - list not seen your promotional email yet:
        -> returns a list of remaining emails
        from combined sets of clients and participants
        that did not seen promotional email yet (recipients set).

    'potential_clients':
    - list of the participants who are not your clients
        -> returns a list of remaining emails from participants set
        that are not existing clients (client set)

    loyalty_program':
    - list of the clients who did not participate in the event.
        -> returns a list of remaining emails
        from clients set that did not
        participated in the event (participants set)
    """

    c_set = set(c_list)
    p_set = set(p_list)
    r_set = set(r_list)
    if task == "call_center":
        return list((c_set | p_set) - r_set)
    elif task == "potential_clients":
        return list(p_set - c_set)
    elif task == "loyalty_program":
        return list(c_set - p_set)


def main():
    """
    Entry point to the program.
    It asses if the argument is 2
    and if the argument
    is in ("call_center", "potential_clients", "loyalty_program")
    calls automate_task() to perform the business task as per action
    """

    clients = [
        'andrew@gmail.com',
        'jessica@gmail.com',
        'ted@mosby.com',
        'john@snow.is',
        'bill_gates@live.com',
        'mark@facebook.com',
        'elon@paypal.com',
        'jessica@gmail.com'
        ]

    participants = [
        'walter@heisenberg.com',
        'vasily@mail.ru',
        'pinkman@yo.org',
        'jessica@gmail.com',
        'elon@paypal.com',
        'pinkman@yo.org',
        'mr@robot.gov',
        'eleven@yahoo.com'
        ]

    recipients = [
        'andrew@gmail.com',
        'jessica@gmail.com',
        'john@snow.is'
        ]

    WRONG_NAME = "Wrong task name is given"

    if len(sys.argv) != 2:
        sys.exit(0)

    try:
        task = sys.argv[1].lower().strip()
        if task not in (
            "call_center",
            "potential_clients",
            "loyalty_program"
        ):
            raise ValueError(WRONG_NAME)
        email_list = automate_task(
            task,
            clients,
            participants,
            recipients
        )
    except ValueError as e:
        print(f"ValueError: {e}")


if __name__ == "__main__":
    main()


"""
Explanation:

main():
    The assesment of argument was from the instruction
    - (Arrange your code in a script.
    The script takes the name of the task
    to perform as an argument:
    call_center, potential_clients, loyalty_program.
    If the wrong name is given, raise an exception.).

    I intuitive assume that the program only takes one argument
    because of the line
    "takes the name of the task to perfom as an argument"
    - singular-> 'an argument'.

    I use lower and split to make the comparison case and whitespace -insensitivity.
    Though its not said to handle it, it also not said not to handle it.
    so i did what i have to do.

automate_task():
    I converted the list inside the function because
    as per instruction the whole business task should be
    done in a separate function.
    I set the lists separately of this line on the instruction
    -("... convert your lists to sets") - plural 'sets'

The word script, i cant really pinpoint if it is a program or just a function,
all i know that script is a sets of instructions based on my own interpretation.
I use main() because of the allowed function sys and also the argument is present
in the instruction.

"""
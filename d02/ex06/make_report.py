from analytics import Research, Analytics
from config import *


def main():
    """
    ->  Validates the arguments.

    ->  Creates an instance of Reseacrch.
        Calls 'file_reader()' Research class method
        with argument True or False - in contingent if
        the file has a header or not-
        to get the content of the file.

        Creates an instace of nested Calculations Class
        with the argument of the data from 'file_reader()'
        and store it as Calculations.lines.

        Calls 'counts()' from nested class Calculations.
        It returns the total counts of head and tails of
        the member Calculations.lines list, and it stores
        the total counts to Calculation.ht_counts.
        the count qualifies if the value is 1.

        Calls 'fraction()' from nested class Calculations
        It returns the fraction percentage of the Calculations.ht_counts
        and stores the fraction percentage to Calculations.ht_fractions.
        formula (num / total) * 100

        Creates an instance of Analytics,
        a child class of nested Calculation class
        from Research Class with the data
        from 'file_read()' as an argument which will
        be stored in Calculations.lines.

        Calls 'predict_random' method
        from Analytics class with the argument
        of an integer that should be greater than 1. It returns
        a list of list random prediction
        using 'randint()'. the length of the items
        are based on the number given.

        Calls 'predict_last' method from Analytics class.
        It returns the last item on the Calculation.lines.


    ->  Raises FileNotFoundError, ValueError, PermissionError, TypeError
        if an error arises.

    Edge Cases:

        main():
            -> if the command line argument is not 2.
            -> if the given argument[1] is not a file.

        file_reader():
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

        _validate_data():
            Iterating on content list.
            -> If the list's items in content does not have a length of 2.
            -> If the list of values within content list are empty.

            Check values:
            -> If the values are not intances of ([0, 1], [1, 0]).

        counts():
            Argument check:
            -> if the passed argument is empty

            Iterate on the list:
            -> if each items on the list has a length of 2
            -> if each values on the items are not int
            -> if each values on the items are either 0 or 1.

        fractions():
            Argument check:
            -> if the items in converted argument to list has a length of 2.
            -> if each items values are digits.

            Zero Division:
            -> if the total of collated counts are zero.

        predict_random():
            Argument check:
            -> if the argument is not integer
            -> if the argument's value is less than 1

        predict_last():
            Argument check:
            -> if the list is empty
               and if the last item of the list is empty.
            -> if the last item's length is not two
               and each value is not an integer.
    """
    try:
        content = Research(file)
        lines = content.file_reader(has_header=True)
        calculations = Research.Calculations(lines)
        analytics = Analytics(lines)

        counts = calculations.counts()
        fractions = calculations.fractions()
        predict_random = analytics.predict_random(num_of_steps)
        p_calc = Research.Calculations(predict_random)
        p_counts = p_calc.counts()

        report = template.format(
            lines=len(lines),
            t_count=counts[1],
            h_count=counts[0],
            t_fraction=fractions[1],
            h_fraction=fractions[0],
            predict=len(predict_random),
            p_t_count=p_counts[1],
            p_h_count=p_counts[0]
            )
        Analytics.save_file(report, filename)

    except (
        FileNotFoundError,
        ValueError,
        PermissionError,
        TypeError,
        IOError
    ) as e:
        print(f"{type(e).__name__}: {e}")

    finally:
        try:
            Research.send_notification(reportfile)
        except (ValueError, RuntimeError) as e:
            print(f"{type(e).__name__}: {e}")

if __name__ == "__main__":
    main()

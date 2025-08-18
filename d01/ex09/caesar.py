import sys


def err_handler(argv: list) -> str | None:
    """
    Returns error message or None.

    Flow:
            -> If the number of arguments is not 4
               it returns 'ERR_ARG' error message

            -> If the argument[1] transformed to lowercase
               and strip whitespaces is not in tuple of task
               'encode' and decode, it returns 'ERR_ION' error
               message

            -> If the argument[2] is not an ascii codes it returns
               'ERR_STR' error message

            -> Use try-except to check if the argument[3] is an integer.
               if it raises a ValueError it returns 'ERR_NUM'
               error message.
               (Used try-except to accomodate negative numbers)

            -> If the conditions above were not met, then it returns
               None.
    """

    ERR_ARG = "Incorrect number of arguments."
    ERR_ION = f"Invalid action: 'decode' or 'encode' only, got {sys.argv[1]}"
    ERR_STR = "The script does not support your language yet."
    ERR_NUM = f"Invalid number: only integer, got {sys.argv[-1]}."

    if len(sys.argv) != 4:
        return ERR_ARG

    if sys.argv[1].lower().strip() not in ("encode", "decode"):
        return ERR_ION

    if not sys.argv[2].isascii():
        return ERR_STR

    try:
        int(sys.argv[3])
    except ValueError:
        return ERR_NUM

    return None


def encode(flr: int, clng: int, code: int, shift: int) -> str:

    """
    Returns the shifted/encrypted letter.

    Flow:

            -> If the sum of ascii number 'code' and 'shift' is
               greater than the ceiling of the
               letter ascii (90|Z or 122|z ),
               it extract the difference and add to
               the floor of the letter ascii (64|A-1 or 96|a-1 )
               and passed to chr() to convert to letter again.

            -> Otherwise it returns the sum of ascii number 'code'
               and 'shift', passed to chr() to convert to letter again.
    """

    return (
        chr(flr + ((code + shift) - clng))
        if (code + shift) > clng
        else chr(code + shift)
    )


def decode(flr: int, clng: int, code: int, shift: int) -> str:

    """
    Returns the shifted/decrypted letter.

    Flow:

            -> If the difference of ascii number 'code' and 'shift' is
               lessthan or equal the ceiling of the
               floor of the letter ascii (64|A-1 or 96|a-1 )
               , it extract the difference and subtract to
               the ceiling of the letter ascii (90|Z or 122|z )
               and passed to chr() to convert to letter again.

            -> Otherwise it returns the difference of ascii number 'code'
               and 'shift', passed to chr() to convert to letter again.
    """

    return (
        chr(clng - (flr - (code - shift)))
        if (code - shift) <= flr
        else chr(code - shift)
    )


def main():

    """
    Prints the encoded or decoded shifted
    argument string by argument number.

    Flow:

            -> Calls the err_handler() and bind
               the return value to 'error' variable.
            -> Asses the 'error' variable if it has
               a valid value/Not empty. If the value
               is a string it raises a ValueError
               and pass the variable 'error' as the
               error message

            -> Bind the arguments needed for the operation
               to variables.
               msg <- string to encrypt and decrypt
               num_shift <- number of shift % 26
               (so that the value will always within 0-26)
               task <- operation if encrypt or decrypt

            -> Initially bind encode() to the 'action' variable
               and asses if the task is equal to "decode" and
               if the 'numshift', then assign decode to 'action'.

            -> Handles if the num_shift is negative value.
               If the task is decode and negative number then
               make the numshift positive and action will be encode.
               If the task is encode and negative number then
               make the numshif positive and action will be decode.
            -> You can imagine that encode() goes clockwise and decode
               counterclockwise. So if the numshift is negative we switch it.
               the the encription uses decode and decription uses encode and
               making the numshift positive.

            -> It iterates to the msg assesing each character
               if it is an alphabet.
            -> It also check if the alphabet is lower or uppercase.
               it both calls the function binded from the 'action'
               variable. the only difference is the floor and ceiling.
            -> the return value of the functions decode and encode will
               be concatinated to the variable 'shifted_msg'.
            -> if it is not an alphabet, the letter will be concatenated with
               'shifted_msg', without any processing.
            -> Once iteration is finished, It prints the 'shifted_msg'

    Legeng:
        Ascii:
        (a - 1) = 64 <- u_flr (Uppercase:
        (A - 1) = 96 <- l_flr
        (z) = 90 <- u_clng
        (Z) = 122 <- l_clng

        (Lowercase: floor,ceiling (96 - 122))
        (Uppercase: floor, ceiling (64 - 90))
    """

    l_flr = 96
    l_clng = 122
    u_flr = 64
    u_clng = 90

    try:
        error = err_handler(sys.argv)
        if error:
            raise ValueError(error)

        msg = sys.argv[2]
        num_shift = int(sys.argv[3]) % 26
        task = sys.argv[1].lower().strip()

        action = encode
        if task == "decode" and num_shift > 0:
            action = decode
        elif task == "decode" and num_shift < 0:
            num_shift *= -1
            action = encode
        elif task == "encode" and num_shift < 0:
            num_shift *= -1
            action = decode

        shifted_msg = ""
        for element in msg.strip():
            if element.isalpha():
                asc_code = ord(element)
                if "a" <= element <= "z":
                    shifted_msg += action(l_flr, l_clng, asc_code, num_shift)
                elif "A" <= element <= "Z":
                    shifted_msg += action(u_flr, u_clng, asc_code, num_shift)
            else:
                shifted_msg += element
        print(shifted_msg)
    except ValueError as e:
        print(f"ValueError: {e}")


if __name__ == "__main__":
    main()

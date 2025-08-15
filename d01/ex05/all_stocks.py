import sys


def company_lookup(arg: str, COMPANIES: dict):
    """
    Returns a list of key value pairs
     if arg is in COMPANIES dictionary,
     otherwise an empty list. 
    """
    for key, value in COMPANIES.items():
        if arg in (value.lower().strip(), key.lower().strip()):
            return [key, value]
    return []


def main():
    """
    Detects and prints wether the argument is company name
    or a ticker symbol, or neither.
    Edge Cases:
    If the argument is not 2 it does nothing.
    If there is empty item on the arg_list.
    Handles case sensitivity and whitespaces.
    """
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }
    ERR_NOTFOUND = "is an unknown company or an unknown ticker symbol"

    if len(sys.argv) != 2:
        sys.exit(0)

    arg_list = [item.lower().strip() for item in sys.argv[1].split(",")]
    for item in arg_list:
        if not item:
            print("")
            sys.exit(0)

    for item in arg_list:
        key_value = company_lookup(item, COMPANIES)
        if not key_value:
            print(f"{item.capitalize()} {ERR_NOTFOUND}")
        else:
            company_name = key_value[0]
            ticker = key_value[1]
            if item == ticker.lower().strip():
                print(f"{ticker} is a ticker symbol for {company_name}")
            elif item == company_name.lower().strip():
                print(f"{company_name} stock price is {STOCKS[ticker]}")


if __name__ == "__main__":
    main()

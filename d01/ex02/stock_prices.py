import sys


def main():

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

    if len(sys.argv) != 2:
        sys.exit(0)

    matching_code = (
        code
        for name, code in COMPANIES.items()
        if name.lower() == sys.argv[1].lower()
        )

    company_code = next(matching_code, None)
    if company_code:
        print(STOCKS[company_code])
    else:
        print("Unknown company")


if __name__ == "__main__":
    main()

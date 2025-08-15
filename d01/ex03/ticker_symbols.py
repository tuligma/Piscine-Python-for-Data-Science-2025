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

    matching_name = (
        name
        for name, code in COMPANIES.items()
        if code.lower() == sys.argv[1].lower()
        )

    company_name = next(matching_name, None)
    if company_name:
        company_price = STOCKS[COMPANIES[company_name]]
        print(f"{company_name} {company_price}")
    else:
        print("Unknown ticker")


if __name__ == "__main__":
    main()

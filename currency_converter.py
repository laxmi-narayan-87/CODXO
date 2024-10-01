exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "JPY": 110.0,
    "GBP": 0.75,
    "INR": 73.5,
    "AUD": 1.4,
    "CAD": 1.3,
    "CHF": 0.92,
    "CNY": 6.45,
    "SEK": 8.6,
    "NZD": 1.5,
    # Add more currencies as needed
}

def convert_currency(amount, from_currency, to_currency, rates):
    try:
        if from_currency != "USD":
            amount = amount / rates[from_currency]
        return amount * rates[to_currency]
    except KeyError:
        return None

def list_available_currencies(rates):
    print("Available currencies:")
    for currency in rates.keys():
        print(currency)

def main():
    while True:
        print("\nCurrency Converter Menu")
        print("1. Convert currency")
        print("2. View available currencies")
        print("3. Exit")
        choice = input("Choose an option (1, 2, 3): ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                from_currency = input("Enter source currency (e.g., USD, EUR): ").upper()
                to_currency = input("Enter target currency (e.g., USD, EUR): ").upper()

                if from_currency in exchange_rates and to_currency in exchange_rates:
                    result = convert_currency(amount, from_currency, to_currency, exchange_rates)
                    if result is not None:
                        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
                    else:
                        print("Error in conversion. Please check the currency codes.")
                else:
                    print("Invalid currency code")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == '2':
            list_available_currencies(exchange_rates)
        elif choice == '3':
            print("Exiting the Currency Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()

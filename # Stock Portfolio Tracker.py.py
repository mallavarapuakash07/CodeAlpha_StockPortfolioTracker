# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 180
}

total_investment = 0

print("----- Stock Portfolio Tracker -----")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Ask user for number of different stocks
number_of_stocks = int(input("How many stocks do you want to add? "))

for i in range(number_of_stocks):
    stock = input("\nEnter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total_investment += value

        print(f"{stock}: ${stock_prices[stock]} × {quantity} = ${value}")
    else:
        print("Stock not available in the list.")

# Display total
print("\n-------------------------------")
print(f"Total Investment Value: ${total_investment}")
print("-------------------------------")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write("------------------------\n")
    file.write(f"Total Investment Value: ${total_investment}\n")

print("Result saved to portfolio.txt")
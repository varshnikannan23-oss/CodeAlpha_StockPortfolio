# Stock Portfolio Tracker
# CodeAlpha Internship - Task 2

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0
portfolio = []

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

while True:

    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:

        quantity = int(input("Enter quantity: "))

        price = stocks[stock_name]
        investment = price * quantity

        portfolio.append({
            "stock": stock_name,
            "quantity": quantity,
            "price": price,
            "investment": investment
        })

        total_investment += investment

        print("Stock Price:", price)
        print("Investment:", investment)

    else:
        print("Stock not found.")
        print("Available stocks:", ", ".join(stocks.keys()))


print("\n================================")
print("          PORTFOLIO")
print("================================")

for item in portfolio:
    print(
        item["stock"],
        "- Quantity:", item["quantity"],
        "- Price:", item["price"],
        "- Investment:", item["investment"]
    )

print("\nTotal Portfolio Investment:", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:

    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("=======================\n\n")

    for item in portfolio:
        file.write(
            f"Stock: {item['stock']}\n"
            f"Quantity: {item['quantity']}\n"
            f"Price: {item['price']}\n"
            f"Investment: {item['investment']}\n\n"
        )

    file.write(
        f"Total Portfolio Investment: {total_investment}\n"
    )

print("\nPortfolio saved to portfolio.txt")
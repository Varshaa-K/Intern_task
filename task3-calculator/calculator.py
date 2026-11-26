
import re
from datetime import datetime, timedelta
from decimal import Decimal, InvalidOperation


def get_positive_amount(prompt):
    value = input(prompt).strip()
    if not re.fullmatch(r"\d+(?:\.\d{1,2})?", value):
        raise ValueError("Enter a valid positive amount (up to 2 decimals).")

    amount = Decimal(value)
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    return amount


def get_inputs():
    name = input("Name: ").strip()
    if not name:
        raise ValueError("Name cannot be empty.")

    card = get_positive_amount("Card balance: ")
    wallet = get_positive_amount("Wallet balance: ")
    meal = get_positive_amount("Cost of one meal: ")
    travel = get_positive_amount("One-way travel cost: ")

    days_input = input("Number of working days: ").strip()
    if not re.fullmatch(r"\d+", days_input) or int(days_input) <= 0:
        raise ValueError("Days must be a positive whole number.")
    days = int(days_input)

    date_input = input("Start date (dd/mm/yyyy): ").strip()
    try:
        start = datetime.strptime(date_input, "%d/%m/%Y").date()
        if start.strftime("%d/%m/%Y") != date_input:
            raise ValueError
    except ValueError:
        raise ValueError("Enter a valid date in dd/mm/yyyy format.")

    return name, card, wallet, meal, travel, days, start


def calculate(card, wallet, meal, travel, days, start):
    travel_total = travel * days
    meal_total = meal * days

    return {
        "travel": travel_total,
        "meal": meal_total,
        "card_balance": card - travel_total,
        "wallet_balance": wallet - meal_total,
        "end_date": start + timedelta(days=days - 1)
    }


def display_summary(name, card, wallet, meal, travel, days, start, result):
    print("\n===== OFFICE COMMUTE SUMMARY =====")
    print(f"Name: {name}")
    print(f"Working days: {days}")
    print(f"Start date: {start:%d/%m/%Y}")
    print(f"End date: {result['end_date']:%d/%m/%Y}")

    print("\n--- Expenses ---")
    print(f"Daily travel: ${travel:.2f}")
    print(f"Total travel: ${result['travel']:.2f}")
    print(f"Daily meal: ${meal:.2f}")
    print(f"Total meals: ${result['meal']:.2f}")

    print("\n--- Remaining Balances ---")
    print(f"Card: ${result['card_balance']:.2f}")
    print(f"Wallet: ${result['wallet_balance']:.2f}")

    for label, balance in [
        ("Card", result["card_balance"]),
        ("Wallet", result["wallet_balance"])
    ]:
        if balance < 0:
            print(f"Insufficient {label} balance by ${-balance:.2f}")
        else:
            print(f"{label} balance is sufficient.")


def main():
    try:
        inputs = get_inputs()
        result = calculate(*inputs[1:])

        display_summary(*inputs[:1], *inputs[1:], result)

    except (ValueError, InvalidOperation, OverflowError) as error:
        print(f"\nInput Error: {error}")


if __name__ == "__main__":
    main()

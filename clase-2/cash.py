# Task list:
# 1. Define bill denomination
# 2. Ask the amount to withdraw, define the bill denomination
# 2. Substract the first denomination


def withdraw_money(amount: int or None = None) -> list[int]:
    amount = ask_number("Ingrese la cantidad a retirar?") if not amount else amount
    denominations: list[int] = [100, 50, 20, 10, 5, 1]  # dollar available bills
    withdrawn: list[int] = []

    for bill in denominations:
        times = amount // bill
        if times > 0 and amount != 0:
            for _ in range(times):
                withdrawn.append(bill)
                amount -= bill
    return withdrawn


def ask_number(prompt: str) -> int:
    prompt = "Enter a number: " if prompt is None else prompt

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    billetes = withdraw_money()
    print(billetes)

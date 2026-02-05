from pathlib import Path
import time

DATA_DIR = Path(__file__).parent / "data"
BALANCE_FILE = DATA_DIR / "balance.txt"
TRANSACTIONS_FILE = DATA_DIR / "transactions.txt"


def ensure_storage():
    DATA_DIR.mkdir(exist_ok=True)
    if not BALANCE_FILE.exists():
        BALANCE_FILE.write_text("0")
    if not TRANSACTIONS_FILE.exists():
        TRANSACTIONS_FILE.write_text("")


def load_balance() -> int:
    return int(BALANCE_FILE.read_text())


def save_balance(balance: int) -> None:
    BALANCE_FILE.write_text(str(balance))


def count_transactions() -> int:
    return len(TRANSACTIONS_FILE.read_text().splitlines())


def load_transactions() -> list[str]:
    return TRANSACTIONS_FILE.read_text().splitlines()


def add_transaction(amount: int, description: str) -> bool:
    balance = load_balance()
    new_balance = balance + amount
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    description = f"{current_time} | {description} | {'+' if amount >= 0 else ''}{amount} | Balance after: {new_balance}"
    if new_balance < 0:
        print("❌ Помилка: баланс не може бути менше 0")
        return False

    with TRANSACTIONS_FILE.open("a") as f:
        f.write(f"{amount}, {description}\n")

    save_balance(new_balance)
    return True


def show_balance():
    balance = load_balance()
    print(f"\n💰 Поточний баланс: {balance}\n")


def show_transactions():
    transactions = load_transactions()

    if not transactions:
        print("\n📭 Транзакцій ще немає\n")
        return

    print("\n📄 Історія транзакцій:")
    for i, transaction in enumerate(transactions, start=1):
        print(f"{i}. {transaction}")
    print()


def main():
    ensure_storage()

    while True:
        print("Оберіть дію:")
        print("1 — Додати транзакцію")
        print("2 — Переглянути баланс")
        print("3 — Переглянути всі транзакції")
        print("0 — Вийти")

        choice = input(">>> ")

        if choice == "0":
            print("👋 До побачення!")
            break

        elif choice == "1":
            try:
                amount = int(input("Введи суму (наприклад 100 або -50): "))
                description = input("Введи призначення: ")
                if add_transaction(amount, description):
                    print("✅ Транзакцію додано\n")
            except ValueError:
                print("❌ Сума має бути цілим числом\n")

        elif choice == "2":
            show_balance()

        elif choice == "3":
            show_transactions()

        else:
            print("❌ Невідома команда\n")


if __name__ == "__main__":
    main()
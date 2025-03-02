from datetime import date
import argparse
import files_manager as fm

class Expense:
    count = 0
    def __init__(self, date, description, amount):
        self.id: int = Expense.count
        self.date: str = date
        self.description: str = description
        self.amount: float = amount
        Expense.count += 1


def menu() -> None:
    parser = argparse.ArgumentParser(description="Expense Tracker, add/remove/update/list expenses.")
    parser.add_argument('-o', '--option', type=str, choices=['add', 'remove', 'update', 'list', 'summary'], required=False, default='add', help='Select the option to add/remove/update/list expenses. (default add)')
    parser.add_argument('-d', '--description', type=str, help="Short description", required=False)
    parser.add_argument('-a', '--amount', type=float, help="Amount of the expense", required=False)

    args = parser.parse_args()

    variables = vars(args)

    config = fm.get_config()
    if config is OSError:
        return
    Expense.count = int(config["expenses_count"])

    match variables['option']:
        case 'add':
            add_expense(variables)
        case 'remove':
            pass
        case 'update':
            pass
        case 'list':
            pass

def add_expense(new_expense: Expense) -> None:
    if new_expense['amount'] is None:
        print("Error. Please enter the expense amount.")
        return

    if new_expense['amount'] <= 0:
        print("Error. The expense amount must be greater than 0.")
        return
    
    if new_expense['description'] is None:
        print("Error. Please enter the expense description.")
        return

    

    expense = Expense(date.today().strftime("%d-%m-%Y"), new_expense['description'], new_expense['amount'])
    print(Expense.count)
    fm.store_expense_in_file(expense)


if __name__ == "__main__":
    menu()
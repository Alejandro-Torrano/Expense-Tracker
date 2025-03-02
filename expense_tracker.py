from datetime import date
import argparse
import files_manager as fm

class Expense:
    last_id = 0
    def __init__(self, date, description, amount):
        self.id: int = Expense.last_id
        self.date: str = date
        self.description: str = description
        self.amount: float = amount


def menu() -> None:
    parser = argparse.ArgumentParser(description="Expense Tracker, add/remove/update/list expenses.")
    parser.add_argument('-o', '--option', type=str, choices=['add', 'remove', 'update', 'list', 'summary'], required=False, default='add', help='Select the option to add/remove/update/list expenses. (default add)')
    parser.add_argument('-d', '--description', type=str, help="Short description", required=False)
    parser.add_argument('-a', '--amount', type=float, help="Amount of the expense", required=False)
    parser.add_argument('-id', '--id', type=int, help="Id of expense", required=False)


    args = parser.parse_args()

    variables = vars(args)

    config = fm.get_config()
    if config is OSError:
        return
    Expense.last_id = int(config["expenses_count"])

    match variables['option']:
        case 'add':
            add_expense(variables)
        case 'remove':
            remove_expense(variables['id'])
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
    if fm.store_expense_in_file(expense_to_dict(expense)) == True:
        if fm.update_expense_count(Expense.last_id + 1) == True:
            Expense.last_id += 1

def remove_expense(expense_id: int) -> None:
    stored_expenses: list[dict] = fm.get_stored_expenses()

    for expense in stored_expenses:
        if expense["id"] == expense_id:
            stored_expenses.remove(expense)
            fm.update_expenses_in_file(stored_expenses)
            break

def expense_to_dict(expense: Expense) -> dict:
    new_dict = {
        "id": expense.id,
        "date": expense.date,
        "description": expense.description,
        "amount": expense.amount
    }

    return new_dict

def dict_to_expense(dict_expense: dict) -> Expense:
    expense = Expense(dict_expense["date"], dict_expense["description"], dict_expense["amount"])
    return expense



if __name__ == "__main__":
    menu()
import json
from expense_tracker import Expense

FOLDER_PATH : str = "Storage/"

def create_file(file_path: str, expense: dict) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump([expense], file, indent=4)

def store_expense_in_file(expense: Expense) -> None:
    _, month, year = expense.date.split("-")
    file_path: str = FOLDER_PATH + year + "-" + month + ".json"
    expense_dict: dict = expense_to_dict(expense)

    stored_expenses: list = get_stored_expenses(file_path)
    if len(stored_expenses) == 0:
        create_file(file_path, expense_dict)
        return
    
    stored_expenses.append(expense_dict)
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(stored_expenses, file, indent=4)
    except:
        print("Error. Can't save the file.")



def get_stored_expenses(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []

def expense_to_dict(expense: Expense) -> dict:
    new_dict = {
        "id": expense.id,
        "date": expense.date,
        "description": expense.description,
        "amount": expense.amount
    }

    return new_dict
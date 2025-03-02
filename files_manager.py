import json

#Este modulo solo acepta y retorna diccionarios


def create_file(file_path: str, expense: dict) -> True:
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump([expense], file, indent=4)
            return True
    except:
        print("Error. Can't create the save file.")
        return False

def store_expense_in_file(expense: dict) -> bool:
    config = get_config()
    file_path: str = config["store_folder_path"] + config["store_file_name"] +".json"

    stored_expenses: list = get_stored_expenses()
    if len(stored_expenses) == 0:
        return create_file(file_path, expense)
    
    stored_expenses.append(expense)
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(stored_expenses, file, indent=4)
            return True
    except:
        print("Error. Can't save the file.")
        return False

def update_expenses_in_file(updated_expenses: list[dict]) -> bool:
    config = get_config()
    file_path: str = config["store_folder_path"] + config["store_file_name"] +".json"
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(updated_expenses, file, indent=4)
            return True
    except:
        print("Error at update the expenses file.")
        return False

def get_stored_expenses() -> list[dict]:
    config = get_config()
    file_path: str = config["store_folder_path"] + config["store_file_name"] +".json"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []

def get_config() -> dict:
    try:
        with open("config.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        print("Error to load the config.")
        return OSError


def update_expense_count(last_expense: int) -> bool:
    config = get_config()
    try:
        with open("config.json", "w", encoding="utf-8") as file:
            config["expenses_count"] = last_expense
            json.dump(config, file, indent=4)
            return True
    except:
        print("Error at update the expenses count.")
        return False

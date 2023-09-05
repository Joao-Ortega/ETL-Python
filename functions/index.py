import requests as api
import csv
import json


def get_random_advice():
    response = api.get("https://api.adviceslip.com/advice")
    return response.json() if response.status_code == 200 else None


def build_advices_to_users(list: list):
    final_arr = []
    for row in list:
        new_list = json.loads(row['FavoritesAdvices'])
        advice = get_random_advice()
        print(f"Loading message => {advice['slip']['advice']}")
        new_list['messages'].append(advice["slip"]["advice"])
        row["FavoritesAdvices"] = new_list
        final_arr.append(row)
    return final_arr


def read_csv_by_path(path: str):
    print(f"Reading {path}...")
    with open(path, mode="r") as csv_file:
        data = csv.DictReader(csv_file)
        message_builded = build_advices_to_users(data)
        return message_builded


def write_on_csv_file(list_treated: list):
    with open("./users_filled.csv", mode="w", newline="") as csv_file:
        field_names = list_treated[0].keys()
        writer = csv.DictWriter(csv_file, field_names)
        writer.writeheader()
        for row in list_treated:
            writer.writerow(row)
    print("Files loaded to: ./users_filled.csv")


def treat_user_file():
    user_agree = input(
        """The csv must have at least a header called FavoritesAdvices
        And its row must be in this format:
        { "messages": [] } Y/N?  """
    )
    if user_agree == "y" or user_agree == "Y":
        user_file = input("Put the path to your file: ")
        if not user_file.endswith(".csv"):
            print("Wrong format. Please insert a csv file!")
            return
        try:
            is_csv_good = read_csv_by_path(user_file)
            return is_csv_good
        except FileNotFoundError:
            print("File not found please verify your file!")
    else:
        return False

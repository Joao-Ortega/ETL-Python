import pandas as pd
import requests as api


def read_csv_by_path(path: str):
    data = pd.read_csv(path).values
    return data


def get_random_advice():
    response = api.get("https://api.adviceslip.com/advice")
    return response
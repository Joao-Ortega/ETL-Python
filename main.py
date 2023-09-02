from functions.index import read_csv_by_path, get_random_advice

path_to_csv = "./users_example.csv"

data = read_csv_by_path(path_to_csv)
advice = get_random_advice()

if advice.status_code == 200:
    print(advice.json())


print(data.tolist())

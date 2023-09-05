from functions.index import (
    read_csv_by_path,
    treat_user_file,
    write_on_csv_file
)


def main():
    user_file = input("Do you want to provide your own csv file? Y/N: ")
    print(user_file)
    if user_file == "y" or user_file == "Y":
        result = treat_user_file()
        write_on_csv_file(result) if result is not False else main()
    else:
        path_to_csv = "./base_file.csv"
        list_to_write = read_csv_by_path(path_to_csv)
        write_on_csv_file(list_to_write)


main()

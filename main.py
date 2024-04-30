users: list[dict] = [
    {"name": "Dawid", "surname": "Bałuka", "posts": 6000},
    {"name": "Kewin", "surname": "Czajkowski", "posts": 6002},
    {"name": "Kamil", "surname": "Gil", "posts": 1_000_000},
    {"name": "Daniel", "surname": "Błaszczyk", "posts": 6}

]


def show_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f"twój znajomy {user['name']} opublikował: {user['posts']} postów")

if __name__ == "__main__":
    print("witaj użytkowniku")
    while True:
        print("wybierz opcję menu:")
        print("1. wyświetl co u znajomych")
        menu_option:str = input("dokonaj wyboru:")
        if menu_option == "o":
            print("program kończy pracę")
            break
        if menu_option == "1":
            show_users(users)

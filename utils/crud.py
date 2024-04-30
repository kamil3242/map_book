def show_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f"twój znajomy {user['name']} opublikował: {user['posts']} postów")
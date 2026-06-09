def login(username, password):
    if username == "admin" and password == "12345":
        return "Вход разрешён"
    else:
        return "Ошибка входа"
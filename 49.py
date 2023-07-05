class UserNotFoundError(Exception):
    pass


users = {
    "alice": {"name": "Alice Smith", "email": "alice@example.com"},
    "bob": {"name": "Bob Johnson", "email": "bob@example.com"},
    "jack": {"name": "Jack Wild", "email": "jack_wild@example.com"}
}


def get_user(username):
    if username in users:
        new_dict=users.get(username)
        return new_dict.get("name")
    else:
        raise UserNotFoundError("User not found")


try:
    username = get_user(input())
except UserNotFoundError as e:
    print(e)
else:
    print(username)

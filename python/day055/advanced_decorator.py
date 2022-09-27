class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
        else:
            print("Not allowed")

    return wrapper


@is_authenticated
def check_is_authenticated(user):
    print(f"This is protected string! Welcome, {user.name}")


new_user = User("Harry")
check_is_authenticated(new_user)

new_user.is_logged_in = True
check_is_authenticated(new_user)

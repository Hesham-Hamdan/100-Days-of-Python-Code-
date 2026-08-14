def logging(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}\nIt returned: {func(*args)}")

    return wrapper


@logging
def a_function(*args):
    print(args)
    return sum(args)


a_function(1, 2, 3)

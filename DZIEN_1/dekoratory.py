#dekoratory w Pythonie
def simple_logger(func):
    def wrapper():
        print("start funkcji")
        func()
        print("koniec funkcji")
    return wrapper

@simple_logger
def hello():
    print("Hello Python!")

def drugi():
    print("\nDrugi tekst!\n")

@simple_logger
def trzeci():
    print("Trzeci tekst!")

hello()
drugi()
trzeci()

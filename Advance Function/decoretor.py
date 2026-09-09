def greet_decorater(func):
    def wrapper():
        print('before greeting')
        func()
        print('after greeting')
    return wrapper

@greet_decorater
def say_hello():
    print('hello......')
say_hello()
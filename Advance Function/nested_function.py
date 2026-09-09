def outer():
    def inner():
        print('inner function called')
    print('outer function started')
    inner()
outer()
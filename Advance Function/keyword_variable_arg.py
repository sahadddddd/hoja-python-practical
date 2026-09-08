def show_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

show_details(name='sahad',age=21,sub='science')
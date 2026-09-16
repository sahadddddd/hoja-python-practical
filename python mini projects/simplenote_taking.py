def write_notes():
    note=input("enter your note:")
    with open("C:\\Users\\DELL\\OneDrive\\Desktop\\hoja python\\python mini projects\\mynotes.text","a") as file:
        file.write(note +"\n")
    print("note saved succesfully")

def read_notes():
    try:
        with open("C:\\Users\\DELL\\OneDrive\\Desktop\\hoja python\\python mini projects\\mynotes.text","r") as file:
            notes=file.readlines()
            if not notes:
                print('no notes found')
            else:
                print('\n----your notes----')
                for line in notes:
                    print(line.strip())
    except FileNotFoundError:
        print("no notes file found yet.write a note first")

def main():
    while True:
        print('\n1.write a new note')
        print("2.view all note")
        print('3.exit')
        choice=input("enter your choice:")

        if choice=='1':
            write_notes()
        elif choice=='2':
            read_notes()
        elif choice=='3':
            print('good bye')
            break
        else:
            print("invalid choice")
main()
def get_password():
    password=input("enter your password:")
    return password

def check_length(password):
    if len(password)>=8:
        return True
    else:
        return False

def check_special_charactor(password):
    special_charecters="! @ # $ % ^ & * ( ) _ + - = ? /" 
    for i in password:
        if i in special_charecters:
            return True
    return False


def check_numbers(password):
    for i in password:
        if i.isdigit():
            return True
        
    return False

def check_uppercase(password):
    for i in password:
        if i.isupper():
            return True
    return False


def display_strength(length_ok,special_ok, number_ok,uppercase_ok):
    score=length_ok+special_ok+ number_ok+uppercase_ok

    print("\n---------------password evaluation-------------------")

    if length_ok:
        print("Length: ✅ PASS (8 or more characters)")
    else:
        print("Length: ❌ FAIL (Less than 8 characters)")

    if special_ok:
        print("Special Character: ✅ PASS")
    else:
        print("Special Character: ❌ FAIL (None found)")

    if number_ok:
        print("Number: ✅ PASS")
    else:
        print("Number: ❌ FAIL (None found)")
    if uppercase_ok:
        print("Uppercase: ✅ PASS")
    else:
        print("Uppercase: ❌ FAIL (None found)")

    print("\n password strength",end='')

    if score <= 1:
        print("WEAK ❌")
    elif score == 2:
        print("MEDIUM ⚠️")
    elif score == 3:
        print("STRONG ✅")
    else:
        print("VERY STRONG 💪")

    print("Total Checks Passed:", score, "/ 4")

def main():
    password=get_password()
    length_ok=check_length(password)
    special_ok=check_special_charactor(password)
    number_ok=check_numbers(password)
    uppercase_ok=check_uppercase(password)

    display_strength(length_ok,special_ok, number_ok,uppercase_ok)

if __name__ =="__main__":
    main()



# another option:
# import re

# def get_password():
#     return input("Enter your password: ")

# def check_length(password):
#     return len(password) >= 8

# def check_special_character(password):
#     special_chars = "!@#$%^&*()_+-=?/"
#     return any(char in special_chars for char in password)

# def check_numbers(password):
#     return any(char.isdigit() for char in password)

# def display_strength(length_ok, special_ok, number_ok):
#     passed_checks = sum([length_ok, special_ok, number_ok])

#     print("\nPassword Strength Evaluation:")
#     print(f"Length check: {'✔️ Passed' if length_ok else '❌ Failed'}")
#     print(f"Special character check: {'✔️ Passed' if special_ok else '❌ Failed'}")
#     print(f"Number check: {'✔️ Passed' if number_ok else '❌ Failed'}")

#     if passed_checks <= 1:
#         print("Strength: WEAK ❌ — Highly vulnerable, improve immediately")
#     elif passed_checks == 2:
#         print("Strength: MEDIUM ⚠️ — Moderate security, missing key elements")
#     else:
#         print("Strength: STRONG ✅ — Excellent security")

# def main():
#     password = get_password()
#     length_ok = check_length(password)
#     special_ok = check_special_character(password)
#     number_ok = check_numbers(password)
#     display_strength(length_ok, special_ok, number_ok)

# if _name_ == "_main_":
#     main()
#PASSWORD STRENGTH CHECK

def check_password_strength():
    print("-Password must be between 8-16 characters long")
    print("-Password must contain at least one capital letter")
    print("-Password must contain at least one digit")
    print("-Password must contain at least one special character (!, @, #, $, %, &, *, ?)")
    print("-Password can not contain spaces")

    retry = True
    while retry == True:

        #Variables/Lists
        special = ['!', '@', '#', '$', '%', '&', '*', '?']
        points = 0
        valid_password = True

        #Password input
        password = input("Please enter your password: ")
        re_enter_pass = input("Please re-enter your password: ")
        while password != re_enter_pass:
            print("Passwords do not match.")
            password = input("Please enter your password: ")
            re_enter_pass = input("Please re-enter your password: ")

        #Restrictions check (Error messages and strength determiner)
        for char in password: #Checking for spaces
            if char == ' ':
                print("Password may not contain spaces.")
                valid_password = False

        if len(password) < 8: #Checking password length
            print("Password not long enough.")
            valid_password = False
        elif len(password) > 16:
            print("Password too long.")
            valid_password = False
        elif 8 <= len(password) < 12:
            points += 1
        elif 12 <= len(password) < 15:
            points += 2
        else:
            points += 3

        has_special = False
        special_count = 0
        for char in password: #Checking for special characters
            if char in special:
                points += 1
                has_special = True
                special_count += 1
            if special_count == 3:
                break
        if has_special == False:
            print("Password must include special character")
            valid_password = False

        has_digit = False
        digit_count = 0
        for char in password: #Checking for digits
            if char.isdigit():
                points += 1
                has_digit = True
                digit_count += 1
            if digit_count == 3:
                break
        if has_digit == False:
            print("Password must include a digit")
            valid_password = False

        checking_case = ''
        for char in password: #Checking for capital letters
            if char.isdigit() == False and char not in special:
                checking_case += char
        if checking_case.islower() == True or checking_case == '':
            print("Password must contain a capital letter")
            valid_password = False
        else:
            points += 1


        #Password strength
        if valid_password == True:
            if 4 <= points <= 6:
                print("Weak password")
            elif 6 < points <= 8:
                print("Moderate password")
            elif points >= 9:
                print("Strong password")
            retry = False
    return password




#CAESAR CIPHER PASSWORD

def caesar_cipher(password):
    shift = input("Number of cipher shifts (Must be 1 more more): ")
    print()
    while shift.isdigit() == False or int(shift) < 1:
        shift = input("Number of shifts: ")
    shift = int(shift)

    encoded_message = ""
    current_ord = 0
    for i in range(len(password)): #Scrambles each character for encoded passsword
        if password[i].isdigit(): #Changes digits
            current_ord = ord(password[i])
            current_ord += shift
            while current_ord > 57:
                current_ord -= 10
            encoded_message += chr(current_ord)
        elif password[i].isalpha(): #Changes letters
            current_ord = ord(password[i])
            current_ord += shift
            if password[i].islower():
                while current_ord > 122:
                    current_ord -= 26
            elif password[i].isupper():
                while current_ord > 90:
                    current_ord -= 26
            encoded_message += chr(current_ord)
        else: #Leaves spaces and special characters the same
            encoded_message += password[i]

    pass_attempt = ""
    pass_correct = False
    for attempt in range(5, 0, -1): #User inputs password to view their encoded password
        print(f"Attempts remaining: {attempt}")
        pass_attempt = input("Please enter your password: ")
        if pass_attempt == password:
            print()
            print(f"Encoded password: {encoded_message}")
            pass_correct = True
            break
        else:
            print("Incorrect.")
        print()
     
    if pass_correct == False: #if user exhausts all 5 attempts their "account" is temporarily deactivated
        print("You are out of attempts. Please try again later.")

password = check_password_strength()
print()
caesar_cipher(password)

import mysql.connector

x = 10
while x > 8:
    print("Welcome, how can I help you today?")
    print("\n1. Manage accounts")
    print("2. Check your balance")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Exit")

    choice = input("\nPlease enter your choice (1-5): ")

    if choice == "1":
        choice2 = input("\nWhat would you like to do? \n1. Create account\n2. Edit account\n3. Delete account\n4. Show account details")
        if choice2 == "1":
            print("\n Please fill out these details to create an account:")
            create_name = input("Name: ")
            create_password = input("Password: ")

            connection = mysql.connector.connect(user='root', password='C#apul1n08', database='banking')
            cursor = connection.cursor()

            query = "INSERT INTO bank_info (name_bank_info, balance_bank_info, user_password) VALUES (%s, %s, %s)"
            values = (create_name, 0.00, create_password)

            cursor.execute(query, values)
            connection.commit()

            print("\nAccount created successfully!")
            cursor.close()
            connection.close()
        elif choice2 == "2":
            print("\nPlease enter an account number: ")
            account_number = input()
            print("\nPlease enter the new name: ")
            new_name = input()
            print("\nPlease enter the new password: ")
            new_password = input()
        elif choice2 == "3":
            print("\nPlease enter the account number you would like to delete: ")
            account_number = input()

            connection = mysql.connector.connect(user='root', password='C#apul1n08', database='banking')
            cursor = connection.cursor()

            query = "DELETE FROM bank_info WHERE id_bank_info = %s"
            values = (account_number,)

            cursir.execute(query, values)
            connection.commit()

            if cursor.rowcount > 0:
                print("\nAccount deleted successfully!")
            else:
                print("\nAccount not found!")
            
            cursor.close()
            connection.close()
        elif choice2 == "4":
            print("\nPlease enter account number you'd like to view:")
            account_number = input()

            connection = mysql.connector.connect(user='root', password='C#apul1n08', database='banking')
            cursor = connection.cursor()

            querey = "SELECT * FROM bank_info WHERE id_bank_info = %s"
            values = (account_number,)

            cursor.execute(query, values)
            result = cursor.fetchone()

            if result:
                stored_password = result[3]
                if entered_password == stored_password:
                    print(f"\nAccount details:")
                    print(f"Account ID:, {result[0]}")
                    print(f"Name:, {result[1]}")
                    print(f"Balance:, ${result[2]:.2f}")
                else:
                    print("\nIncorrect password!")
            else:
                print("\nAccount not found!")

            cursor.close()
            connection.close()
    elif choice == "2":
        print("\nPlease enter your account number: ")
        account_number = input()
        print("\nPlease enter your password: ")
        entered_password = input()

        connection = mysql.connector.connect(user='root', password='C#apul1n08', database='banking')
        cursor = connection.cursor()

        query = "SELECT balance_bank_info, user_password FROM bank_info WHERE id_bank_info = %s"
        values = (account_number,)

        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            stored_balance = result[0]
            stored_password = result[1]

            if entered_password == stored_password:
                print(f"\nYour balance is: ${stored_balance:.2f}")
            else:
                print("\nIncorrect password!")
        else:
            print("\nAccount not found!")

        cursor.close()
        connection.close()
#continue with deposit and withdraw options
    elif choice == "3":
        print("\nPlease enter your account number: ")
        account_number = input()
        print("Please specify the amount you would like to deposit: ")
    elif choice == "4":
        #in development, not yet implemented
        pass
    elif choice == "5":
        print("Thank you for banking with us, goodbye!")
        x = 6
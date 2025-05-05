print("Welcome, how can I help you today?")
print("\n1. Manage accounts")
print("2. Check your balance")
print("3. Deposit money")
print("4. Withdraw money")
print("5. Transfer money")
print("6. Exit")

choice = input("\nPlease enter your choice (1-6): ")

if choice == "1":
    choice2 = input("\nWhat would you like to do? \n1. Create account\n2. Edit account\n3. Delete account\n")
    if choice2 == "1":
        #in development, not yet implemented
        pass
    elif choice2 == "2":
        #in development, not yet implemented
        pass
    elif choice2 == "3":    
        #in development, not yet implemented
        pass
    pass
elif choice == "2":
    #in development, not yet implemented
    pass
elif choice == "3":
    #in development, not yet implemented
    pass
elif choice == "4":
    #in development, not yet implemented
    pass
elif choice == "5":
    #in development, not yet implemented
    pass
elif choice == "6":
    print("Thank you for banking with us, goodbye!")

INSERT INTO bank_info (id_bank_info, name_bank_info, balance_bank_info)
VALUES
('10294', 'Xavier', '1200.00')
('10295', 'Joe', '1500.00');
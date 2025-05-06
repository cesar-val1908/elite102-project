#was having issues with the sql connector last night, havent tried anything yet today
#also having issues with trying to create a virtual environment.

import mysql.connector

#testing connection to the database
connection = mysql.connector.connect(user='root', password='C#apul1n08', database='Local instance MySQL80 (banking)')
print("Connection successful!")
connection.close()

#HIGHLIGHT AND RUN SEPARATELY TO TEST, ONCE ITS CLEAR THAT IT WORKS THEN EDIT  

#trying to add data to the database
connection = mysql.connector.connect(user = 'root', database = 'Local instance MySQL80 (banking)',  password = 'C#apul1n08')
cursor = connection.cursor()

addData = ("INSERT INTO bank_info (id_bank_info, name_bank_info, balance_bank_info) VALUES(%s, %s, %s)")
values = ("10294", "Xavier", "1200.00")
cursor.execute(addData, values)
connection.commit()
cursor.close()
connection.close()


#this will check what is in the database, and print it to the console
#this is just for testing purposes, to see if the connection works and if the database is set up correctly
#testQuery = ("SELECT * FROM bank_info")
#cursor.execute(testQuery)

#for item in cursor:
#    print(item)



print("Welcome, how can I help you today?")
print("\n1. Manage accounts")
print("2. Check your balance")
print("3. Deposit money")
print("4. Withdraw money")
print("5. Exit")

choice = input("\nPlease enter your choice (1-5): ")

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
    print("Thank you for banking with us, goodbye!")
    pass

#INSERT INTO bank_info (id_bank_info, name_bank_info, balance_bank_info)
#VALUES
#('10294', 'Xavier', '1200.00')
#('10295', 'Joe', '1500.00');



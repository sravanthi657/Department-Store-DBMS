
In the Final Database,

Changes made from Relational model are:

The Primary Key of the ADMIN Relation now comprises of (Admin_ID,Date_On)
Also this change satisfies the 1NF,2NF and 3NF too.


Execution of the program:
$ Run docker start (container id)
$ mysql -u root -p < billing.sql
"Enter your mysql password"
$ python3 INCOGNITO.py

Enter your username
Enter your mysql password
In case of wrong credentials for connection, a prompt telling "Connection Refused" appears.
If not: Enter any key to procced to queries

Instructions for choosing a query appears with 10 options to choose from.

Functional Requirements:
Enter 1: To Insert new customer details
Enter the values into the fields, in the order the prompt asks
If values are inserted successfully prompt tells "Inserted"

Enetr 2: To Insert new Product details
Enter the values into the fields, in the order the prompt asks
If values are inserted successfully prompt tells "Inserted"

Enter 3:To Delete Product of Sale details for returned products
Enter the values into the fields, in the order the prompt asks
If values are entered successfully and deletion occurs, prompt tells "Deleted"

Enetr 4:To View Customer's details who gave Assisstance Feedback lesser than 4
Enter the values into the fields, in the order the prompt asks
If successful, prints the asked rows.

Enter 5:To View Admin ID's of Admins with maximum number of shifts in any given period
Enter the values into the fields, in the order the prompt asks
Prints the ID of the Admin

Enter 6:To View a Customer's preferred Modes of Payment for all payments
Enter the values into the fields, in the order the prompt asks
Prints a table with the required fields.

Enter 7:To Insert Reporting details of an Admin
Enter the values into the fields, in the order the prompt asks
Prints a table with the required fields.

Enter 8:To Update the Active Points of a Member
Enter the values into the fields, in the order the prompt asks
Prompt tells that update happened and show points available after update

Enter 9:To Update the Active Points of a Non Member
Enter the values into the fields, in the order the prompt asks
Prompt tells that update happened and show points available after update

Enter 10:To Update price of existing Products
Enter the values into the fields, in the order the prompt asks
Prompt tells the final price after  update.

In case of wrong data type inputs, violation of constraints or unsuccessful query, the prompt 
"-----Failed-----"
"Try Again"
appears for any query.




import pymysql
import pymysql.cursors
import subprocess as pp

def option4():
    try:
        query="select * from CUSTOMER where Admin_Assisstance_Feedback<=3"
        cur.execute(query)
        rows=cur.fetchall()
        print("Number of such Customers=",cur.rowcount)
        for r in rows:
            print(r)
    except Error as e:
        print("-----Failed-----")
        print("Try Again")
    return

def option1():
    try:
        row={}
        print("Enter new Customer details")
        row["First_Name"]=input("First Name:")
        row["Last_Name"]=input("Last Name:")
        row["Email_ID"]=input("Email ID:")
        row["Mobile_Number"]=int(input("Mobile Number"))
        row["Admin_Assisstance_Feedback"]=int(input("Feedback(A scale of 1-5, where 1 is very disappointed and 5 is satisfied:"))
        row["Date_of_Birth"]=input("Date_of_Birth(YYYY-MM-DD)")
        row["Admin_ID"]=int(input("Admin ID"))
        query = "INSERT INTO CUSTOMER(First_Name,Last_Name,Email_ID,Mobile_Number,Admin_Assisstance_Feedback,Date_of_Birth,Admin_ID) VALUES('%s', '%s', '%s', %d, %d, '%s' ,%d)" % (row["First_Name"], row["Last_Name"], row["Email_ID"], row["Mobile_Number"], row["Admin_Assisstance_Feedback"], row["Date_of_Birth"], row["Admin_ID"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted")
    except Exception as e:
        con.rollback()
        print("-----Failed-----")
        print("Try Again")
    return

def option2():
    try:
        row={}
        print("Enter new Product details")
        row["Product_ID"]=input("Product ID:")
        row["Price_per_Unit"]=int(input("Enter price per each unit:"))
        row["Unit"]=input("Select one unit type from litres,kilograms,dozens, units:")
        row["Admin_ID"]=int(input("Enter Admin ID:"))
        query = "INSERT INTO PRODUCT(Product_ID,Price_per_Unit,Unit,Admin_ID) VALUES('%s',%d, '%s' ,%d)" %(row["Product_ID"],row["Price_per_Unit"],row["Unit"],row["Admin_ID"])
        print(query)
        cur.execute(query)
        con.commit()
        print("Inserted")
    except Exception as e:
        con.rollback()
        print("-----Failed-----")
        print("Try again")

    return

def option3():
    try:
        Mobile=int(input("Enter Returning Customers Mobile Number:"))
        Sale_ID=int(input("Enter Sale_ID of returning product:"))
        Sale_Products=input("Enter product to be returned")
        query="DELETE FROM PRODUCTS_OF_SALE WHERE (Customer_Mobile ='%d' AND SALE_ID='%d' AND Sale_Products='%s') "%(Mobile,Sale_ID,Sale_Products)
        print(query)
        cur.execute(query)
        con.commit()
        print("Deleted")
    except Exception as e:
        con.rollback()
        print("-----Failed-----")
        print("Try again")
    return

def option5():
    try:
        start=input("Enter starting date(YYYY-MM-DD):")
        end=input("Enter ending date(YYYY-MM-DD):")
        query="select count(Admin_ID),Admin_ID from ADMIN where (Date_on<='%s' AND Date_On>='%s') group by Admin_ID"%(end,start)
        cur.execute(query)
        rows=cur.fetchall()
        x=rows[0]['count(Admin_ID)']
        y=rows[0]['Admin_ID']
        for r in rows:
            if r['count(Admin_ID)']>x:
                x=r['count(Admin_ID)']
                y=r['Admin_ID']
        for w in rows:
            if w['count(Admin_ID)']==x:
                print("Maximum shifts in the given time are worked\nby Admin with ID",w['Admin_ID'],end='')
                print(",worked shifts:",x)



    except Exception as e:
        con.rollback()
        print("-----Failed-----")
        print("Try again")
    return

def option6():
    try:
        mobile=int(input("Enter Mobile Number: "))
        query= "select Customer_Mobile,count(*),Mode_of_Payment from PAYMENT where Customer_Mobile='%d' group by Mode_of_Payment"%(mobile)
        cur.execute(query)
        r=cur.fetchall()
        for x in r:
            print(x)
        q1="select Mobile_Number from MEMBER"
        cur.execute(q1)
        r1=cur.fetchall()
        c=0
        for x1 in r1:
            if x1['Mobile_Number']==mobile:
                c=1;
                break
        if c==1:
            print("Customer is a Member")
        else:
            print("Customer is not a Member")

    except Exception as e:
        con.rollback()
        print("-----Failed-----")
        print("Try again")
    return

def report_admin():
	try:
		a_tuple={}
		print("Enter the  Reporting details of an Admin: ")
		a_tuple["Admin_ID"]=  int(input("Admin ID: "))
		a_tuple["Date_On"]= input("Reporting Date: ")
		a_tuple["Time_at"]= input("Reporting Time: ")
		a_tuple["Reported_Admin_ID"]=int(input("Reported Admin ID: "))
		query="INSERT INTO ADMIN(Admin_ID,Date_On,Time_at,Reported_Admin_ID) VALUES('%d','%s','%s','%d')"%(a_tuple["Admin_ID"],a_tuple["Date_On"],a_tuple["Time_at"],a_tuple["Reported_Admin_ID"])
		cur.execute(query)
		con.commit()
		print("Inserted Into Database")
	except Exception as e:
		con.rollback()
		print("-----Failed-----")
		print ("Try Again")
        
	return

def update_mem_points():
	try:
            mem_id = int(input("Enter the Membership Id: "))
            reedem_points=int(input("Enter the Points gained: "))
            query="UPDATE MEMBERSHIP SET Membership_points=Membership_points+'%d' WHERE (Membership_ID='%d')"%(reedem_points,mem_id)
            cur.execute(query)
            con.commit()
            query1="select Membership_Points from MEMBERSHIP where Membership_ID='%d'"%(mem_id)
            cur.execute(query1)
            r=cur.fetchall()
            print("Member's points gained are updated")
            print("Available Points are" ,r)
		
	except Exception as e:
		con.rollback()
		print("-----Failed-----")
		print ("Try Again")
        
	return
	        

def update_nonmem_points():
	try:
            mobile = int(input("Enter the Mobile Number: "))
            reedem_points=int(input("Enter the Points gained: "))
            query="UPDATE NON_MEMBER SET Points_Active=Points_Active+'%d' WHERE (Mobile_Number='%d')"%(reedem_points,mobile)
            cur.execute(query)
            con.commit()
            query1="select Points_Active from NON_MEMBER where Mobile_Number='%d'"%(mobile)
            cur.execute(query1)
            r=cur.fetchall()
            print("Non-Member Points gained are updated")
            print("Available points are",r)
		
	except Exception as e:
		con.rollback()
		print("-----Failed-----")
		print ("Try Again")
        
	return
def update_price():
	try:
            product_id=int(input("Enter Product id to be updated"))
            price=int(input("Enter newprice per unit"))
            query="update PRODUCT SET Price_per_Unit='%d' where Product_ID='%d'"%(price,product_id)
            cur.execute(query)
            con.commit()
            print("Updated price per unit is now",price)
	except Exception as e:
		con.rollback()
		print("-----Failed-----")
		print("Try Again")


def communicate (ch):

    if(ch==1):
        option1()
    if(ch==2):
        option2()
    if(ch==3):
        option3()
    if(ch==4):
        option4()
    if(ch==5):
        option5()
    if(ch==6):
        option6()
    if(ch==7):
        report_admin()
    if(ch==8):
        update_mem_points()
    if(ch==9):
        update_nonmem_points()
    if(ch==10):
        update_price()
	
    


while(1):
    tmp = pp.call('clear', shell=True)
    username = input("Username: ")
    password = input("Password: ")
    try:
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='billing',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = pp.call('clear', shell=True)
        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("\nEnter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = pp.call('clear', shell=True)
                print("\n Enter 1 to Insert new Customer details")
                print("\n Enter 2 to Insert new Product details")
                print("\n Enter 3 to Delete Product of Sale details for returned products")
                print("\n Enter 4 to View Customer's details who gave Assisstance Feedback lesser than 4")
                print("\n Enter 5 to View Admin ID's of Admins with maximum number of shifts in any given period")
                print("\n Enter 6 to View a Customer's preferred Modes of Payment for all payments")
                print("\n Enter 7 to Insert Reporting details of an Admin") 
                print("\n Enter 8 to Update the Active Points of a Member")  
                print("\n Enter 9 to Update the Active Points of a Non-member")
                print("\n Enter 10 to Update price of existing Products")
                ch = int(input("\n Enter choice-----> "))
                tmp = pp.call('clear', shell=True)
                if ch == 11:
                    break
                else:
                    communicate(ch)
                    tmp = input("Enter any key to CONTINUE>")
    except:
        tmp = pp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")

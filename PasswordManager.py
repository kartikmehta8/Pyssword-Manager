"""
PASSWORD MANAGER

This Password Manager uses MySQL for storing the Passwords!
Follow the Steps given below to setup the Password Manager for your Computer...

Open MySQL & enter your password...

STEP 1 : CREATE DATABASE password;
STEP 2 : USE password;
STEP 3 : CREATE TABLE record (SerialNo int(3), Name varchar(25), Password varchar(25));
STEP 4 : Change the variable ver (line 30) and password (line 35) to your MySQL Password.
STEP 5 : Go to cmd and type - 'pip install mysql-connector-python'
YOU ARE READY TO BEGIN!!!
"""

def space():
    print()
    print()
    
print("Welcome to Password Manager!")
print("          -By Kartik Mehta")
space()

app='y'
while app=='y':
    space()
    ver=input("To continue... Enter the Master Password : ")
    space()
    if ver=='YOUR_PASSWORD':#Set the Password as same as of your MySQL Password or from which you want to authenticate yourself...
        space()
        print("Password Authentication Successful!")
        space()
        import mysql.connector
        mydb=mysql.connector.connect(host='localhost',user='root',password='YOUR_PASSWORD',database='password') #Set the Password as same as of your MySQL Password!
        mycursor=mydb.cursor()
        if mydb.is_connected():
            space()
            print("Connected to the Database Successfully!")
            space()
            print("Enter the action :- ")
            space()
            print("1. View passwords")
            print("2. Add Password")
            print("3. Update Password")
            print("4. Delete Password")
            print("5. Remove All Records")
            space()
            ch=input("Enter the Choice : ")
            space()
            if ch=='1':
                print("Showing all the records present in the database..........")
                space()
                mycursor.execute("SELECT * from record;")
                print("SrNo. ,","Name ,","Password")
                for x in mycursor:
                    print(x)
                space()
            elif ch=='2':
                space()
                add='y'
                while add=='y':
                    aaa='y'
                    while aaa=='y':
                        try:
                            mycursor.execute("SELECT max(SerialNo) from record;")
                            for i in mycursor:
                                print("The last Serial No. observed : ",i)
                            space()
                            serial=int(input("Enter the Serial Number : "))
                            space()
                            break
                        except ValueError:
                            space()
                            print("Please enter a VALID Number....")
                            space()
                            aaa=input("Do you want to retry? [y/n] : ")
                            space()
                    if aaa!='y':
                        break
                    space()
                    name=input("Enter the Name of Website/Domain : ")
                    space()
                    pswd=input("Enter Password : ")
                    space()
                    repswd=input("Re-enter the Password : ")
                    if pswd==repswd:
                        space()
                        print("Password Matched")
                        space()
                        print("Adding Your Record.....")
                        space()
                        query="INSERT into record values (%s,%s,%s)"
                        values=(serial,name,pswd)
                        mycursor.execute(query,values)
                        mydb.commit()
                        space()
                        print(mycursor.rowcount,'Password Inserted Successfully!')
                        space()
                        add=input("Do you want to enter more? [y/n] : ")
                        space()
                    else:
                        space()
                        print("Sorry, the password does not match....")
                        space()
                        add=input("Do you want to retype? [y/n] : ")
                        if add=='y':
                            continue
                        else:
                            space()
                            print("No New Record Is Added....")
                            space()
                else:
                    space()
            elif ch=='3':
                space()
                add='y'
                while add=='y':
                    print("Please select of which Website/Domain you wanted to update the Password :")
                    space()
                    mycursor.execute("SELECT Name from record;")
                    for i in mycursor:
                        print(i)
                    space()
                    upd=input("Enter : ")
                    space()
                    pswde=input("SET the New Password : ")
                    ps=input("Confirm New Password Again : ")
                    if pswde==ps:
                        space()
                        print("New Password Confirmed!")
                        query="UPDATE record SET password = %s where Name = %s;"
                        values=(pswde,upd)
                        mycursor.execute(query,values)
                        mydb.commit()
                        space()
                        print("Password Updated Successfully.....")
                        space()
                        break
                    else:
                        space()
                        print("New Password Confirmation Failed.....")
                        space()
                        add=input("Do you want to retry? [y/n] : ")
                        space()
                        if add=='y':
                            continue
                        else:
                            space()
                            print("No Password is Updated....")
                            space()
            elif ch=='4':
                space()
                add='y'
                while add=='y':
                    print("Please select the Website name of which you wanted to delete the Password......")
                    space()
                    mycursor.execute("select Name from record;")
                    for i in mycursor:
                        print(i)
                    space()
                    dell=input("Enter : ")
                    space()
                    query='DELETE from record where Name = %s;'
                    value=(dell,)
                    mycursor.execute(query,value)
                    mydb.commit()
                    space()
                    print("Password DELETED Successfully.....")
                    space()
                    add=input("Do you want to delete more? [y/n] : ")
                    space()
            elif ch=='5':
                space()
                print("You are about to DELETE all the records from the table......")
                space()
                print("To continue, enter the PASSCODE as shown : ")
                space()
                import random
                import string
                yaa='y'
                while yaa=='y':
                    letters=string.ascii_lowercase
                    ran=''.join(random.choice(letters) for i in range(6))
                    space()
                    print("PASSCODE : ",ran)
                    space()
                    con=input("Enter : ")
                    if con==ran:
                        space()
                        mycursor.execute("DELETE from record;")
                        mydb.commit()
                        print("All the records have been deleted.....")
                        space()
                        break
                    else:
                        space()
                        print("Passcode does not match....")
                        space()
                        yaa=input("Do you want to retry? [y/n] : ")
                        space()
                else:
                    space()
                    print("Nothing Deleted!")
                    space()
            else:
                space()
                print("Please Enter among the Specified choices ONLY.....")
                space()
    else:
        space()
        print("Sorry, the password is wrong!")
        space()
    space()
    app=input("Do you wish to continue? [y/n] : ")
    space()
else:
    space()
    print("Thank You!")
    space()

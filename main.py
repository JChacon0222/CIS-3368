#Jacob Chacon CIS 3368 HW 1

#imports
import mysql.connector


#connecting to mysql database
mydb = mysql.connector.connect(#to access database https://www.w3schools.com/python/python_mysql_getstarted.asp
  host="cis3368.cipzgffy5aqa.us-east-1.rds.amazonaws.com",
  user="admin",
  password="Password"
)

#giving initial menu options for user to pick from
print("MENU")
print("a - Add car")
print("d - Remove car")
print("u - Update car details")
print("r1 - Output all cars sorted by year (ascending)")
print("r2- Output all cars of a certain color")
print("q - Quit")
#getting initial user response
response = input("Please select an option")

#while loop to repeat while options are selected
while response != "q":
    print("MENU")
    print("a - Add car")
    print("d - Remove car")
    print("u - Update car details")
    print("r1 - Output all cars sorted by year (ascending)")
    print("r2- Output all cars of a certain color")
    print("q - Quit")
    response = input("Please select an option")

    if response == "a":
        #collecting info to add row
        userid = input("id")
        usermake = input("make")
        usermodel = input("model")
        useryear = input("year")
        usercolor = input("color")
        mycursor = mydb.cursor()
        sql = "INSERT INTO Garage (id, make, model, year, color) VALUES (%s, %s, %s, %s, %s,)"
        val = (userid, usermake, usermodel, useryear, usercolor)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        response = input("Please select another menu option")

    elif response == "d":
        #collecting info on which id to delete
        userid = input("id")
        mycursor = mydb.cursor()
        sql = "DELETE FROM Garage WHERE id = userid
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
        response = input("Please select another menu option")

    elif response == "u":
        #collecting which id to update
        userid = input("id")

        #collecting how to update
        usermake = input("make")
        usermodel = input("model")
        useryear = input("year")
        usercolor = input("color")

        mycursor = mydb.cursor()
        sql1 = "UPDATE Garage SET make = usermake WHERE id = userid"
        sql2 = "UPDATE Garage SET model = usermodel WHERE id = userid"
        sql3 = "UPDATE Garage SET year = useryear WHERE id = userid"
        sql4 = "UPDATE Garage SET color = usercolor WHERE id = userid"
        #execute each update
        mycursor.execute(sql1)
        mycursor.execute(sql2)
        mycursor.execute(sql3)
        mycursor.execute(sql4)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        response = input("Please select another menu option")

    elif response == "r1":
        #sorting by year acsending
        mycursor = mydb.cursor()
        sql = "SELECT * FROM Garage ORDER BY year"
        mycursor.execute(sql)
        yearsorted = mycursor.fetchall()
        for x in yearsorted:
            print(x)
        response = input("Please select another menu option")

    elif response == "r2":
        usercolor = input("color")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM Garage WHERE color =usercolor"
        mycursor.execute(sql)
        colorsorted = mycursor.fetchall()
        for x in colorsorted:
            print(x)
        response = input("Please select another menu option")

    else:
        #if user enters incorrect option
        print("Please enter a valid response")
        response = input("Please select an option")

#closing statement when user chooses to quit "q"
print("_________________")
print("Thank you!")
print("Have a great day!")
print("_________________")

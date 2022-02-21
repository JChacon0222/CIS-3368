#Jacob Chacon CIS 3368 HW 1

#imports
import mysql.connector


#connecting to mysql database
mydb = mysql.connector.connect(#to access database https://www.w3schools.com/python/python_mysql_getstarted.asp
  host="cis3368.cipzgffy5aqa.us-east-1.rds.amazonaws.com",
  user="admin",
  password="Password"
)

#giving initial menu options
print("MENU")
print("a - Add car")
print("d - Remove car")
print("u - Update car details")
print("r1 - Output all cars sorted by year (ascending)")
print("r2- Output all cars of a certain color")
print("q - Quit")
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
        userid = input("id")
        mycursor = mydb.cursor()
        sql = "DELETE FROM Garage WHERE id = userid
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")

        response = input("Please select another menu option")

    elif response == "u":
        userid = input("id")


        usermake = input("make")
        usermodel = input("model")
        useryear = input("year")
        usercolor = input("color")

        mycursor = mydb.cursor()
        sql = "UPDATE Garage SET make = usermake WHERE id = userid"
        sql = "UPDATE Garage SET model = usermodel WHERE id = userid"
        sql = "UPDATE Garage SET year = useryear WHERE id = userid"
        sql = "UPDATE Garage SET color = usercolor WHERE id = userid"
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        response = input("Please select another menu option")

    elif response == "r1":
        mycursor = mydb.cursor()
        sql = "SELECT * FROM Garage ORDER BY year"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        response = input("Please select another menu option")

    elif response == "r2":
        usercolor = input("color")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM Garage WHERE color =usercolor"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        response = input("Please select another menu option")

    else:
        print("Please enter a valid response")
        response = input("Please select an option")

#closing statement when user chooses to quit
print("_________________")
print("Thank you!")
print("Have a great day!")
print("_________________")

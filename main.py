import mysql.connector

mydb = mysql.connector.connect(#to access database https://www.w3schools.com/python/python_mysql_getstarted.asp
  host="cis3368.cipzgffy5aqa.us-east-1.rds.amazonaws.com",
  user="admin",
  password="Password"
)

#print(mydb)




    print("MENU")
    print("a - Add car")
    print("d - Remove car")
    print("u - Update car details")
    print("r1 - Output all cars sorted by year (ascending)")
    print("r2- Output all cars of a certain color")
    print("q - Quit")



while response != "q":
    print("MENU")
    print("a - Add car")
    print("d - Remove car")
    print("u - Update car details")
    print("r1 - Output all cars sorted by year (ascending)")
    print("r2- Output all cars of a certain color")
    print("q - Quit")

    if response = "a":
        mycursor = mydb.cursor()

        sql = "INSERT INTO Garage (id, make, model, year, color) VALUES (%s, %s, %s, %s, %s,)"
        val = ("17", "Honda", "Accord", "2002", "White")
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

    elif response = "d":
        mycursor = mydb.cursor()

        sql = "DELETE FROM Garage WHERE id = 'Mountain 21'"

        mycursor.execute(sql)

        mydb.commit()

        print(mycursor.rowcount, "record(s) deleted")

    elif response = "u":

    elif response = "r1":

    elif response = "r2":

    else:
        print("Please enter a valid response")




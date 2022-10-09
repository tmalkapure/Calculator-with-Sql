from flask import Flask, request, render_template
#from flaskext.mysql 
import mysql.connector as sql



def sql_connector():
    mydb = sql.connect(user="root",password="tushar1234", db="db_cal", host="localhost")
    #conn = pymysql.connect(user='root', password='password', db='pehla', host='localhost')
    mycursor = mydb.cursor()
    #c = conn.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS db_cal")
    print("DB is already created")
    return mydb, mycursor
 
def InsertIntoCalculatorTable(num1, num2, operation, result):
    count = mycursor.execute("SELECT COUNT(*) from calculator")
    count = mycursor.fetchone()[0]
    count+=1
    mycursor.execute("INSERT INTO db_cal.calculator VALUES ({}, {}, {}, {}, {})".format((count), int(operation), int(num1), int(num2), int(result)))
    mydb.commit()  
#mydb = sql.connect(host="localhost",user="root",password="pavan8189")

#mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE IF NOT EXISTS Db_calculator")
#print("DB is already created")
app = Flask(__name__)
global count
@app.route("/", methods =["GET", "POST"])
def salvador():
    if request.method == "POST":
       operation = request.form.get("intvalue")
       # getting input with name = fname in HTML form
       num1 = request.form.get("num1")
       # getting input with name = lname in HTML form
       num2 = request.form.get("num2")
       #mydb, mycursor = sql_connector()
       #mycursor.execute("INSERT INTO Db_calculator.calculate VALUES ({}, {}, {}, {}, {}, {})".format(int(1), int(intvalue), int(num1), int(num2), int(result)))
       #mydb.commit()
       
       if operation == "1":
            result = int(num1) + int(num2)
            InsertIntoCalculatorTable(num1,num2,1,result)

            #count = mycursor.execute("SELECT COUNT(*) from calculator")
            #count = mycursor.fetchone()[0]
            #count+=1
            #mycursor.execute("INSERT INTO db_cal.calculator VALUES ({}, {}, {}, {}, {})".format((count), int(operation), int(num1), int(num2), int(result)))
            #mydb.commit()
            return "addition is "+str(result)
            #return render_template('home2.html', result=result)

       elif operation == "2":
            result = int(num1) - int(num2)
            InsertIntoCalculatorTable(num1,num2,2,result)
            #count = mycursor.execute("SELECT COUNT(*) from calculator")
            #count = mycursor.fetchone()[0]
            #count+=1
            #mycursor.execute("INSERT INTO db_cal.calculator VALUES ({}, {}, {}, {}, {})".format((count), int(operation), int(num1), int(num2), int(result)))
            #mydb.commit()
            return "substraction is "+str(result)
            #return render_template('home2.html', result=result)

       elif operation == "3":
            result = int(num1) * int(num2)
            InsertIntoCalculatorTable(num1,num2,3,result)
            #count = mycursor.execute("SELECT COUNT(*) from calculator")
            #count = mycursor.fetchone()[0]
            #count+=1
            #mycursor.execute("INSERT INTO db_cal.calculator VALUES ({}, {}, {}, {}, {})".format((count), int(operation), int(num1), int(num2), int(result)))
            #mydb.commit()
            return "multiplication is "+str(result)
            #return render_template('home2.html', result=result)

       elif operation == "4":
            try:
                result = int(num1) / int(num2)
                count = mycursor.execute("SELECT COUNT(*) from calculator")
                count = mycursor.fetchone()[0]
                count+=1
                mycursor.execute("INSERT INTO db_cal.calculator VALUES ({}, {}, {}, {}, {})".format((count), int(operation), int(num1), int(num2), int(result)))
                mydb.commit()
                return "division is "+str(result)
            except ZeroDivisionError:
                return "Can't divide by zero"

       mycursor.close()
       #return 'success' 
    return render_template("home2.html")   
       
if __name__ == "__main__":
    mydb, mycursor = sql_connector()
    count = 0
    count = mycursor.execute("SELECT COUNT(*) from calculator")
    count = mycursor.fetchone()[0]
    print (count)
            
    app.run(debug=True)

import mysql.connector

#function to validate user exists
def validate_user(username, password):
    #user info query
    sql_query = "SELECT * FROM `maintable` WHERE username=\'" + username + "\'"

    #database connectivity
    mydb = mysql.connector.connect(
        host="Bgross21.mysql.pythonanywhere-services.com",
        database="Bgross21$accounts",
        user="Bgross21",
        password="VYFIKJB817364"
    )

    mycursor = mydb.cursor() # enables us to create SQL queries
    mycursor.execute(sql_query) # We execute sql queries
    myresult = mycursor.fetchall()# result of query

    # There is no user by the username
    if len(myresult) == 0:
        return False #user does not exist in database
    else:
        #user exists, now check pass
        u = myresult[0][0]
        p = myresult[0][1]
        if username == u and password == p:
            return True
        else:
            return False


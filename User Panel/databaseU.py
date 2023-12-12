import mysql.connector
Info = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="recodir"
)
cursor = Info.cursor()

def loginAdmin(data):
    try:
        cursor.execute('SELECT * FROM `add_teacher` WHERE `Username` = %s AND `Password` = %s', data)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False  
      
# ---------------MATERIAL-------------------- 
#Register
def registerMaterial(data):
    try:
        cursor.execute('INSERT INTO `add_material` ( `course`, `Department`, `Subject`,`Topic`) VALUES (%s, %s, %s,%s)', data)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
#read
def getMaterial():
    try:
        cursor.execute('SELECT * FROM `add_material`')
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return []

def getbytopic(id):
    try:
        query = "SELECT Course, Department, Subject,Topic FROM `add_material` WHERE id = %s"
        cursor.execute(query, id)
        return cursor.fetchone()   
    except Exception as e:
        print(e)
        return []
#update
def updateMaterial(old_topic,new_course,new_department,new_subject,new_topic):
    try:
        query = "UPDATE `add_material` SET Course = %s, Department = %s, Subject = %s,Topic = %s WHERE Topic = %s"
        data=(new_course,new_department,new_subject,new_topic,old_topic)
        cursor.execute(query,data)
        Info.commit()
        return True
    except Exception as e:
        print(e)
#delete
def delMaterial(id):
    try:
        cursor.execute('DELETE FROM `add_material` WHERE `id` = %s', id)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
    
#-------------------ASSIGNMENT----------------------------- 
#Register
def registerAssignment(data):
    try:
        cursor.execute('INSERT INTO `add_assignment` ( `course`, `department`, `subject`,`number`) VALUES (%s, %s, %s,%s)', data)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
#read
def getAssignment():
    try:
        cursor.execute('SELECT * FROM `add_assignment`')
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return []
    
def getbyassignment(id):
    try:
        query = "SELECT course, department, subject,number FROM `add_assignment` WHERE id = %s"
        cursor.execute(query, id)
        return cursor.fetchone()   
    except Exception as e:
        print(e)
        return []
#update
def updateAssignment(old_number,new_course,new_department,new_subject,new_number):
    try:
        query = "UPDATE `add_assignment` SET course = %s, department = %s, subject = %s,number = %s WHERE number = %s"
        data=(new_course,new_department,new_subject,new_number,old_number)
        cursor.execute(query,data)
        Info.commit()
        return True
    except Exception as e:
        print(e)
#delete
def delAssignment(id):
    try:
        cursor.execute('DELETE FROM `add_assignment` WHERE `id` = %s', id)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False

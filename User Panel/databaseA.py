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
        cursor.execute('SELECT * FROM `admin_login` WHERE `Username` = %s AND `Password` = %s', data)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False
    
#------------TEACHER------------------------------  
def registerTeacher(data):
    try:
        cursor.execute('INSERT INTO `add_teacher` ( `Name`, `Contact`, `Qualification`, `Username`,`Password`) VALUES (%s, %s, %s,%s,%s)', data)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
def getTeacher():
    try:
        cursor.execute('SELECT * FROM `add_teacher`')
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return []
def getbyusername(id):
    try:
        query = "SELECT Name, Contact, Qualification, Username FROM `add_teacher` WHERE id = %s"
        cursor.execute(query, id)
        return cursor.fetchone()   
    except Exception as e:
        print(e)
        return []  
      
def updateTeacher(old_username, new_name, new_contact, new_qualification, new_username):
    try:
        query = "UPDATE `add_teacher` SET Name = %s, Contact = %s, Qualification = %s, Username = %s WHERE Username = %s"
        data = (new_name, new_contact, new_qualification, new_username,old_username)
        cursor.execute(query, data) 
        Info.commit()
        return True
    except Exception as e:
        print(e)
        
def delTeacher(id):
    try:
        cursor.execute('DELETE FROM `add_teacher` WHERE `id` = %s', id)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
#----------------------COURSE-----------------------  
def registerCourse(data):
    try:
        cursor.execute('INSERT INTO `add_course` ( `Name`, `Duration`, `Cost`) VALUES (%s, %s, %s)', data)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def getCourse():
    try:
        cursor.execute('SELECT * FROM `add_course`')
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return []
def getbycourse(id):
    try:
        query = "SELECT Name, Duration, Cost FROM `add_course` WHERE id = %s"
        cursor.execute(query, id)
        return cursor.fetchone()   
    except Exception as e:
        print(e)
        return []
    
def updateCourse(old_name, new_name, new_duration, new_cost):
    try:
        query = "UPDATE `add_course` SET Name = %s, Duration = %s, Cost = %s WHERE Name = %s"
        data = (new_name, new_duration, new_cost,old_name)
        cursor.execute(query, data) 
        Info.commit()
        return True
    except Exception as e:
        print(e)
    
def delCourse(id):
    try:
        cursor.execute('DELETE FROM `add_course` WHERE `id` = %s', id)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False

#---------------------SUBJECT------------------------------------   
def registerSubject(data):
    try:
        cursor.execute('INSERT INTO `add_subject` ( `Degree`, `Course`, `Name`) VALUES (%s, %s, %s)', data)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def getSubject():
    try:
        cursor.execute('SELECT * FROM `add_subject`')
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return []
    
def getbysubject(id):
    try:
        query = "SELECT Degree, Course, Name FROM `add_subject` WHERE id = %s"
        cursor.execute(query, id)
        return cursor.fetchone()   
    except Exception as e:
        print(e)
        return []
    
def updateSubject(old_name, new_degree, new_course, new_name):
    try:
        query = "UPDATE `add_subject` SET Degree = %s, Course = %s, Name = %s WHERE Name = %s"
        data = (new_degree, new_course, new_name,old_name)
        cursor.execute(query, data) 
        Info.commit()
        return True
    except Exception as e:
        print(e)
    
def delSubject(id):
    try:
        cursor.execute('DELETE FROM `add_subject` WHERE `id` = %s', id)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def getCourseName():
    try:
        cursor.execute("SELECT Name FROM `add_course`")
        return cursor.fetchall()
    except Exception as e:
        print(e)

def getSubjectName():
    try:
        cursor.execute("SELECT Name FROM `add_subject`")
        return cursor.fetchall()
    except Exception as e:
        print(e)
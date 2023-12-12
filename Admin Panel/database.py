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
def loginUser(data):
    try:
        cursor.execute('SELECT * FROM `add_teacher` WHERE `Username` = %s AND `Password` = %s', data)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False
    
#------------TEACHER------------------------------  
def registerTeacher(data):
    try:
        cursor.execute('INSERT INTO `add_teacher` ( `Name`, `Contact`, `Qualification`, `Username`,`Password`,`Subject`) VALUES (%s, %s, %s,%s,%s,%s)', data)
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
        query = "SELECT Name, Contact, Qualification, Username, Subject FROM `add_teacher` WHERE id = %s"
        cursor.execute(query, id)
        return cursor.fetchone()   
    except Exception as e:
        print(e)
        return []  
      
def updateTeacher(id, new_name, new_contact, new_qualification, new_username,new_subject):
    try:
        query = "UPDATE `add_teacher` SET Name = %s, Contact = %s, Qualification = %s, Username = %s ,Subject=%s WHERE id = %s"
        data = (new_name, new_contact, new_qualification, new_username,new_subject,id[0])
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
    
def updateCourse(id, new_name, new_duration, new_cost):
    try:
        query = "UPDATE `add_course` SET Name = %s, Duration = %s, Cost = %s WHERE id = %s"
        data = (new_name, new_duration, new_cost,id[0])
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
    
def updateSubject(id, new_degree, new_course, new_name):
    try:
        query = "UPDATE `add_subject` SET Degree = %s, Course = %s, Name = %s WHERE id = %s"
        data = (new_degree, new_course, new_name,id[0])
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

def pieview():
    try:
        cursor.execute('SELECT COUNT(*) FROM `add_teacher`')
        staff_count = cursor.fetchone()[0]  # Get the count for "addstaff" table
        cursor.execute('SELECT COUNT(*) FROM `add_subject`')
        student_count = cursor.fetchone()[0]  # Get the count for "addstudent" table
        
        return staff_count, student_count  # Return the counts for both tables
    except Exception as e:
        print(e)
        return None  # Handle the error condition appropriately
def barview():
    try:
        cursor.execute('SELECT COUNT(*) FROM `add_teacher`')
        staff_count = cursor.fetchone()[0]  # Get the count for "addstaff" table
        cursor.execute('SELECT COUNT(*) FROM `add_course`')
        student_count = cursor.fetchone()[0]  # Get the count for "addstudent" table
        cursor.execute('SELECT COUNT(*) FROM `add_subject`')
        course_count = cursor.fetchone()[0]
        return staff_count, student_count ,course_count # Return the counts for both tables
    except Exception as e:
        print(e)
        return None  # Handle the error condition appropriately
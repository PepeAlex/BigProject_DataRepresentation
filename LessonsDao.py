import mysql.connector
import dbconfig as cfg

class LessonsDao:
    db = " "
    def __init__(self):
        self.db = mysql.connector.connect(
        host = cfg.mysql['host'],
        user = cfg.mysql['user'],
        password = cfg.mysql['password'],
        database = cfg.mysql['database']
        )
    
    # Create
    def create(self, lessons):
        cursor = self.db.cursor()
        sql = "insert into lessons (id, lecturer, subject, delivered, price) values (%s, %s, %s, %s, %s)"
        values = [
            lessons["id"],
            lessons["lecturer"],
            lessons["subject"],
            lessons["delivered"], 
            lessons["price"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    # Get All
    def getAll(self): 
        cursor = self.db.cursor()
        sql = "select * from lessons" 
        cursor.execute(sql)
        results = cursor.fetchall()  
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        
        return returnArray

    def findById(self, id):
        cursor = self.db.cursor()
        sql = "select * from lessons where id = %s"
        values = [ id ] 
        cursor.execute(sql, values)
        results = cursor.fetchone()  
        return self.convertToDict(results)

    def update(self, lessons):
        cursor = self.db.cursor()
        sql = "update lessons set lecturer = %s, subject = %s, delivered = %s, price = %s where id = %s"
        values = [
            lessons["lecturer"],
            lessons["subject"],
            lessons["delivered"], 
            lessons["price"],
            lessons["id"]
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return lessons

    def delete(self, id):
        cursor = self.db.cursor()
        sql = "delete from lessons where id = %s"
        values = [ id ] 
        cursor.execute(sql, values)
        self.db.commit()
        return {}

    
    def convertToDict(self, results):
        colnames = ["id", "lecturer", "subject", "delivered", "price"]
        lessons = {}

        if results:
            for i, colName in enumerate(colnames):
                value = results[i]
                lessons[colName] = value

        return lessons

lessonDao = LessonsDao()
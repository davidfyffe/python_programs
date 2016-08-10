#!/usr/bin/env python
#import sqlite3

class DatabaseController:
    'Common button controller class. takes pin number in constructor'
    
    
    
    def __init__(self):
        self.amount = 6
        print ""
        #self.conn = sqllite3.connect('localDB.db')
        
    def insertInitialValue(self):
        print "Database Controller: insert initial value"
        #c = self.conn.cursor()
        #c.execute("INSERT INTO servoposition VALUES('init', 0)")
            
    def updateValue(self, pos):
        #c = self.conn.cursor()
        #c.execute('''UPDATE servoposition SET position = ?''', pos)
        #conn.commit()
        print "Database Controller: updating to ", pos
        self.amount = pos
    
    def deleteValue(self):
        print "delete"
        #c = self.conn.cursor()
        #c.execute('''DELETE FROM servoposition''')
    
    def selectValue(self):
        #c = self.conn.cursor()
        #c.execute('''SELECT position FROM servoposition''')
        print "Database Controller: returning ", self.amount
        return self.amount #c.fetchone()
        
    def createTable(self):
        print "Database Controller: creating table"
        #c = self.conn.execute('''CREATE TABLE servoposition(changesource text, position real)''')
        #conn.commit();


#db = DatabaseController()
#db.createTable()
#db.insertInitialValue()
#db.updateValue(7)
#print db.selectValue()

#!/usr/bin/env python
import sqlite3


class DatabaseController:
    'Common button controller class. takes pin number in constructor'
    
    def __init__(self):
        #self.amount = 6
        print "Database Controller: Constructor"
        
        
    def insertInitialValue(self):
        print "Database Controller: insert initial value"
        self.conn = sqlite3.connect('localDB.db')
        c = self.conn.cursor()
        c.execute("INSERT INTO servoposition VALUES('init', 0)")
        self.conn.commit()
        self.conn.close()
            
    def updateValue(self, pos):
        self.conn = sqlite3.connect('localDB.db')
        c = self.conn.cursor()
        c.execute('''UPDATE servoposition SET position = ?''', (float(pos),))
        self.conn.commit()
        self.conn.close()
        print "Database Controller: updating to ", pos
        #self.amount = pos
    
    def deleteValue(self):
        self.conn = sqlite3.connect('localDB.db')
        print "delete"
        c = self.conn.cursor()
        c.execute('''DELETE FROM servoposition''')
        self.conn.commit()
        self.conn.close()
    
    def selectValue(self):
        self.conn = sqlite3.connect('localDB.db')
        c = self.conn.cursor()
        c.execute('''SELECT position FROM servoposition''')
        val = c.fetchone()
        print "Database Controller: returning ", val
        #return self.amount #
        self.conn.close()
        return val[0]
        
    def createTable(self):
        self.conn = sqlite3.connect('localDB.db')
        print "Database Controller: creating table"
        c = self.conn.cursor()
        c.execute('''CREATE TABLE servoposition(changesource text, position real)''')
        self.conn.commit()
        self.conn.close()
        
    def dropTable(self):
        self.conn = sqlite3.connect('localDB.db')
        print "Database Controller: dropping table"
        c = self.conn.cursor()
        c.execute('''DROP TABLE servoposition ''')
        self.conn.commit()
        self.conn.close()


#db = DatabaseController()
#db.dropTable()
#db.createTable()
#db.insertInitialValue()
#db.updateValue(7)
#print db.selectValue()

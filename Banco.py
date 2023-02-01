import psycopg2
import Error as error
class Banco():
    
    def __init__(self, tbName):
        try:
            self.conn = psycopg2.connect(database='pabd', 
                        host='localhost', 
                        user='postgres', 
                        password='ifrn123', 
                        port='5432')
        except psycopg2.OperationalError as e:
            return error.Error.exceptions(e)
            
        self.cursor = self.conn.cursor()
        self.tbName = tbName
        
    def selectOne(self, idSensor):
        self.cursor.execute("SELECT * FROM {} WHERE idsensor = {};".format(self.tbName, idSensor))
        return self.cursor.fetchone()

    def selectAll(self):
        self.cursor.execute("SELECT * FROM {}".format(self.tbName))
        return self.cursor.fetchall()
    
    def deleteOne(self, idSensor):
        self.cursor.execute("DELETE FROM {} WHERE idsensor = {};".format(self.tbName, idSensor))    
        
    def insertOne(self, idSensor, variavel, medicao, unidade, registro, latitutde, longitude):
        self.cursor.execute("INSERT INTO {} VALUES ({},'{}',{},'{}','{}',{},{}) RETURNING idSensor;".format(self.tbName, idSensor, variavel, medicao, unidade, registro, latitutde, longitude))    
        return self.cursor.fetchone()      
    
    def updateOne(self, idSensor, variavel, medicao, unidade, registro, latitude, longitude):
        self.cursor.execute("UPDATE {} SET variavel='{}', medicao={}, unidade='{}', registro='{}', latitude={}, longitude={} WHERE idSensor = {};".format(self.tbName, variavel, medicao, unidade, registro, latitude, longitude,idSensor))
        
    def commitChanges(self):
        self.conn.commit()
    
    def closeConnection(self):
        self.conn.close()
    
    def rollbackConnection(self):
        self.conn.rollback()
        
from Banco import Banco
import Error as error
import psycopg2
class Model():
    def __init__(self, tbName):
        self.banco = Banco(tbName)
    
    def read_one_sensor(self, idSensor):
        try:
            return self.banco.selectOne(idSensor)
        except psycopg2.Error as e:
            error.Error.print_psycopg2_exception(e)
        finally:
            self.banco.rollbackConnection()
        
    def read_all_sensors(self):
        try:
            return self.banco.selectAll()
        except psycopg2.Error as e:
            error.Error.print_psycopg2_exception(e)
        finally:
            self.banco.rollbackConnection()
    
    def delete_one_sensor(self, idSensor):
        try:
            self.banco.deleteOne(idSensor)
        except psycopg2.Error as e:
            return error.Error.exceptions(e)
        
    def insert_one_sensor(self, idSensor, variavel, medicao, unidade, registro, latitutde, longitude):
        try:
            if(self.banco.insertOne(idSensor, variavel, medicao, unidade, registro, latitutde, longitude)):
                return "Sensor inserido com sucesso!"
        except psycopg2.Error as e:
            return error.Error.exceptions(e)
        finally:
            self.banco.rollbackConnection()

    def update_one_sensor(self, idSensor, variavel, medicao, unidade, registro, latitutde, longitude):
        self.banco.updateOne(idSensor, variavel, medicao, unidade, registro, latitutde, longitude);
    
    def commit_changes(self):
        self.banco.commitChanges()
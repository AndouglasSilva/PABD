from tkinter import *
from Relatorio import *
import pandas as pd

class Controller():
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.setCommandSearch(self.buscarSensor)
        self.view.setCommandInsert(self.insertSensor)
        self.view.setCommandDelete(self.deleteSensor)
        self.view.setCommandUpdate(self.updateSensor)
        self.view.setCommandGenerateReport(self.gerarRelatorio)
        self.view.setCommandCommit(self.commitBanco)
        
    def buscarSensor(self):
        idSensor = self.view.txtidSensor.get()
        sensor  = self.model.read_one_sensor(idSensor)
        self.view.updateBySearch(sensor)
    
    def insertSensor(self):
        idSensor = self.view.txtidSensor.get()
        variavel = self.view.txtVariavel.get()
        medicao = self.view.txtMedicao.get()
        unidade = self.view.txtUnidade.get()
        registro = self.view.txtRegistro.get()
        latitude = self.view.txtLatitude.get()
        longitude = self.view.txtLongitude.get()
        
        msg = self.model.insert_one_sensor(idSensor, variavel, medicao, unidade, registro, latitude, longitude)
        self.view.logInsert(msg)
    
    def deleteSensor(self):
        idSensor = self.view.txtidSensor.get()
        self.model.delete_one_sensor(idSensor)
        self.view.logDelete()
        
    def updateSensor(self):
        idSensor = self.view.txtidSensor.get()
        variavel = self.view.txtVariavel.get()
        medicao = self.view.txtMedicao.get()
        unidade = self.view.txtUnidade.get()
        registro = self.view.txtRegistro.get()
        latitude = self.view.txtLatitude.get()
        longitude = self.view.txtLongitude.get()
        
        self.model.update_one_sensor(idSensor, variavel, medicao, unidade, registro, latitude, longitude);
        self.view.logUpdate(idSensor);
                
    def commitBanco(self):
        self.model.commit_changes()
        
    def gerarRelatorio(self):
        #Teste usando DataFrame
        df = pd.DataFrame(self.model.read_all_sensors());
        df.columns = ["idSensor", "variavel","valor", "unidade", "registro", "latitude", "longitude"]
        print(df)
        Relatorio.build_pdf(df)
        
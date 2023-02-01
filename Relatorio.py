from fpdf import FPDF
import pandas as pd

class Relatorio(FPDF):
    def add_page(self):
        FPDF.add_page(self)
        #Configuração do estilo do cursor 
        self.set_font("Arial", style="U", size=12)
        
        #Escrita do título Relatório de BD no topo da página.
        #O número 190 corrende ao posicionamento em x e 30 o posicionamento em y
        self.cell(190, 30, txt="Relatório de BD", ln=1, align='C')
        
        #Agora colocamos o cursos na posição x=10 e y=50
        self.set_xy(10,50)
        
        #Alteramos o tamanho do cursos para 8
        self.set_font("Arial", size=8)
        
    
    def build_pdf(data):
        pdf = Relatorio()
        pdf.add_page()
        
        #Este vetor contém valores de tamanho para cada coluna do banco de dados (valores obtidos no chute!)
        col_width_vector = [18, 20, 15, 15, 45, 30, 30]
        col_width = 0
        #Este primeiro laço de reptição correponde ao nome de cada coluna no banco
        #Essa informação está contida na variável data.columns
        for col in data.columns:
            pdf.cell(col_width_vector[col_width], 10, col, border=1)
            col_width = col_width + 1
        pdf.set_xy(10,60)
        row_height = pdf.font_size
        
        #Este segundo laço de reptição correponde a escrita de cada valor
        #Cada linha (row) da tabela é obtida por meio da matriz data.values      
        for row in data.values:
            col_width = 0  
            for item in row:
                pdf.cell(col_width_vector[col_width], row_height, str(item), border=1) 
                col_width = col_width + 1
            pdf.ln()
        
        #Salvamos o relatório aqui!
        pdf.output('relatorio_bd.pdf', 'F')
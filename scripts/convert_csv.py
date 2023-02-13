import sys
import pandas as pd
  # referências: https://towardsdatascience.com/how-to-export-pandas-dataframe-to-csv-2038e43d9c03
  # referências: https://colab.research.google.com/drive/1R6SHFugbCEuy5ppjDFymquj3jjbgY7Sx?authuser=1

def convert_csv():
  #xlsx_file_path = "upload/Modelo_Sesp_Feminicdio.Jan20_Dez22.xlsx"
  #abas = ["Dados"]
  #for aba in abas:
    #read_file = pd.read_excel (xlsx_file_path, aba)
    #abas.rename(columns = {'TENTADO/CONSUMADO':'TENTADO_CONSUMADO','DATA DO FATO':'DATA_FATO','MÊS':'MES','ANO DO FATO':'ANO_FATO','MUNICIPIO DO FATO':'MUNICIPIO_FATO','QTD DE VÍTIMAS':'QTD_VITIMAS'}, inplace=True)
    #read_file.to_csv (f'data/feminicidio-2020-2022.csv', index = None, header=True, sep = ';', decimal = ',', encoding = 'utf-8-sig', na_rep = "")
    feminicidio = pd.read_excel('http://www.seguranca.mg.gov.br/images/2023/Janeiro/Modelo_Sesp_Feminicdio.Jan20_Dez22.xlsx', sheet_name='Dados')
    feminicidio.rename(columns = {'TENTADO/CONSUMADO':'TENTADO_CONSUMADO','DATA DO FATO':'DATA_FATO','MÊS':'MES','ANO DO FATO':'ANO_FATO','MUNICÍPIO DO FATO':'MUNICIPIO_FATO','QTD DE VÍTIMAS':'QTD_VITIMAS'}, inplace=True)
    feminicidio = pd.read_excel('http://www.seguranca.mg.gov.br/images/2023/Janeiro/Modelo_Sesp_Feminicdio.Jan20_Dez22.xlsx', sheet_name='Dados', names=feminicidio.columns, header=0)
    feminicidio.to_csv (f'data/feminicidio-2020-2022.csv', index = None, header=True, sep = ';', decimal = ',', encoding = 'utf-8-sig', na_rep = "")
    violencia = pd.read_excel('http://www.seguranca.mg.gov.br/images/2023/Janeiro/Modelo_Sesp_Violencia%20Domestica%20e%20Familiar%20contra%20a%20Mulher.Jan20_Dez22.xlsx', sheet_name='Dados')
    violencia.rename(columns = {'MUNICÍPIO-CÓD':'MUNICIPIO_COD','MUNICÍPIO':'MUNICIPIO','DATA DO FATO':'DATA_FATO','MÊS':'MES','QUANT. VÍTIMAS VIOL.DOMÉSTICA':'QUANT_VITIMAS_VIOL.DOMESTICA'}, inplace=True)
    violencia = pd.read_excel('http://www.seguranca.mg.gov.br/images/2023/Janeiro/Modelo_Sesp_Violencia%20Domestica%20e%20Familiar%20contra%20a%20Mulher.Jan20_Dez22.xlsx', sheet_name='Dados', names=violencia.columns, header=0)
    violencia.to_csv (f'data/violencia-contra-mulher-2020-2022.csv', index = None, header=True, sep = ';', decimal = ',', encoding = 'utf-8-sig', na_rep = "")
if __name__ == '__main__':
  convert_csv()

# AttributeError: module 'sys' has no attribute 'arg'

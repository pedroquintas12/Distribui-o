import xlrd
import openpyxl
import pandas as pd
import re
from docx import Document
import mysql.connector
import os
from datetime import datetime, timedelta

data_do_dia = datetime.now()
data_formatada = data_do_dia.strftime('%Y%m%d')
nomeDoArquivo = (data_formatada + "-" + "impressao.xls")
nomeDoArquivoDocx = (data_formatada + "-" + "distribuição.docx")

caminho_arquivo = r"C:\Users\pedro\OneDrive - LIG CONTATO DIÁRIO FORENSE\DISTRIBUIÇÃO\DISTRIBUIÇÕES\\" + nomeDoArquivo

if not os.path.exists(caminho_arquivo):
    data_do_dia -= timedelta(days=1)  
    data_formatada = data_do_dia.strftime('%Y%m%d')
    nomeDoArquivo = (data_formatada + "-" + "impressao.xls")
    caminho_arquivo = r"C:\Users\pedro\OneDrive - LIG CONTATO DIÁRIO FORENSE\DISTRIBUIÇÃO\DISTRIBUIÇÕES\\" + nomeDoArquivo
    nomeDoArquivoDocx = (data_formatada + "-" + "distribuição.docx")


print("Caminho do arquivo:", caminho_arquivo)

try:
    workbook= xlrd.open_workbook(caminho_arquivo)
    sheet= workbook.sheet_by_index(0)
    print("Planilha carregada")

    #colunas para ser extraidas (coluna 0 == coluna 1 da tabela original)
    colunas_alvo=[0, 2, 4, 5, 7, 10, 12]
    
    dados_das_linhas = []

    nome_coluna_tratamento = 'coluna_5'

    for row in range(1, sheet.nrows):  # Começando da segunda linha                                                                                                         
        linha = {}

        for col_idx, col in enumerate(colunas_alvo):
            valor_celula = sheet.cell_value(row, col)
            nome_coluna = f'coluna_{col + 1}'

            if col == 4:
                valor_celula = re.sub(r'[^\w\s| \w\s-]', '', valor_celula) #remove todos os caractes especiais menos "|"
                valor_celula = re.sub(r'\d+|CNPJ', '', valor_celula, flags=re.IGNORECASE)
                valor_celula = re.sub(r'\d+|LTDA', '', valor_celula, flags=re.IGNORECASE)
                valor_celula = re.sub(r'\d+|CPF', '', valor_celula, flags=re.IGNORECASE)
                valor_celula = re.sub(r'\d+|EM PERNAMBUCO', '', valor_celula, flags=re.IGNORECASE)

                valor_celula = valor_celula.strip() #tira o espaçamento
                
            





except FileNotFoundError:
    print("Arquivo Excel não encontrado.") 
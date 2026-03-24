# 1. Ler os arquivos (funcao extract)
# 2. Concatenar os arquivos (funcao extract)
# 3. Transformar os arquivos
# 4. load dos arquivos (decidir por 2 caminhos)
import pandas as pd
import os
import glob
#listar arquivos (pode usar ls como no termimal)

# funcao de extract que le e consolida os json
def extrair_dados_e_consolidar(pasta: str ) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json')) #lendo os arquivos
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json] #listando os arquivos
    df_total = pd.concat(df_list,  ignore_index=True) #concatenando os arquivos
    return df_total

# uma funcao que transforma
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


#para saber se é csv, parquet ou ambos

def carregar_dados(df: pd.DataFrame, format_saida: list):
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados.csv")
        if formato == "parquet":
            df.to_parquet("dados.parquet")

def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)


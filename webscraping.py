import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://resultados.bajasaebrasil.net/prova.php?id=24BR_GER"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", id="myTable")

cabecalho = [el.text.strip() for el in table.find_all("th")]
rows = []
for row in table.find_all("tr")[1:]:  #! Ignorar a primeira linha (cabeçalho)
    rows.append([el.text.strip() for el in row.find_all("td")])

#! Mostrar os dados coletados no terminal (remover o '#')
#print("Cabeçalho:", cabecalho)
#for row in rows:
#    print("Equipes:", row)

#! DataFrame
cabecalho = ['Pos. final', 'Num. carro', 'Equipe/Escola', 'Região', 'Penalidade', 'Segurança', 'Projeto', 'Dinâmicas', 'Enduro', 'Bônus 4x4', 'Total']
df = pd.DataFrame(rows, columns=cabecalho)

#! Salvando em Excel
arquivo = "resultados_equipes.xlsx"
df.to_excel(arquivo, index=False)

print(f"Os dados foram salvos no arquivo '{arquivo}' com sucesso!")
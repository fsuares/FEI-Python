import pandas as pd

nomes = pd.read_json('https://servicodados.ibge.gov.br/api/v2/censos/nomes/')
print(nomes)
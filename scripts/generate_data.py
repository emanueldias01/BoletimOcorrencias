from faker import Faker
from boletim_ocorrencias.repositories.database import DataBase
import random

fake = Faker("pt_BR") 

db = DataBase() 

registros = []

for _ in range(1000): 
    registro = {
        "data_registro": fake.date_this_year().strftime("%Y-%m-%d"),
        "tipo_ocorrencia": random.choice(["Furto", "Roubo", "Agressão", "Vandalismo", "Perda"]),
        "descricao": fake.sentence(nb_words=6),
        "status": random.choice(["Aberto", "Em análise", "Fechado"]),
        "nome_declarante": fake.name(),
        "nome_autor": fake.name()
    }
    registros.append(registro)

db.insert(registros)
print("1.000 registros gerados e inseridos com sucesso!")

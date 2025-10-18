from faker import Faker
import random
from boletim_ocorrencias.database import DataBase

import os
import csv


db = DataBase()

os.makedirs(db.base_path, exist_ok=True)

csv_path = db.csv_path
seq_path = db.seq_path

if not os.path.exists(csv_path):
    with open(csv_path, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(
            arquivo,
            fieldnames=["id", "data_registro", "tipo_ocorrencia", "descricao", "status", "nome_declarante", "nome_autor", "deleted"]
        )
        escritor.writeheader()

        if not os.path.exists(seq_path):
            with open(seq_path, "w", encoding="utf-8") as arquivo:
                arquivo.write("0")



fake = Faker("pt_BR") 

registros = []

for _ in range(1000): 
    registro = {
        "data_registro": fake.date_this_year().strftime("%Y-%m-%d"),
        "tipo_ocorrencia": random.choice([
            "Furto", "Roubo", "Homicídio", "Lesão Corporal", "Ameaça", 
            "Violência Doméstica", "Estelionato", "Danos Materiais", 
            "Acidente de Trânsito", "Embriaguez ao Volante", 
            "Desaparecimento de Pessoa", "Encontro de Cadáver", 
            "Encontro de Pessoa", "Perturbação do Sossego/Tranquilidade", 
            "Violação de Domicílio", "Dano", "Posse de Drogas", 
            "Tráfico de Drogas", "Porte Ilegal de Arma", "Receptação", 
            "Crime Cibernético", "Fraude", "Difamação", "Injúria", "Calúnia", 
            "Desobediência", "Desacato", "Violação de Medida Protetiva", 
            "Tentativa de Suicídio", "Maus-tratos a Animais", "Outros"
        ]),
        "descricao": fake.sentence(nb_words=6),
        "status": random.choice([
            "Registrado", "Em Análise", "Em Investigação", "Complementado", 
            "Encaminhado", "Suspenso", "Arquivado", "Concluído", 
            "Cancelado", "Aguardando Validação", "Reaberto"
        ]),
        "nome_declarante": fake.name(),
        "nome_autor": fake.name()
    }
    registros.append(registro)

db.insert(registros)

print("1.000 registros gerados e inseridos com sucesso!")

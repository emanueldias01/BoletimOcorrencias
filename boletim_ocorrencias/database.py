import csv
import json

class DataBase:


    def __init__(self):
        with open("boletim.csv", "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=["id", "data_registro", "tipo_ocorrencia", "descricao", "status", "nome_declarante", "nome_autor", "deleted"])
            writer.writeheader()
        
        with open("boletim.seq", "w") as arquivo:
            arquivo.write('0')

        print("Criado com sucesso")

    def next_id(self):
        with open("boletim.seq", "r+") as arquivo:
            prev_id = int(arquivo.readline())
            next_id = prev_id + 1
            arquivo.seek(0)
            arquivo.write(str(next_id))
        return prev_id

    def insert(self, dados_boletim):
        with open("boletim.csv", "a", newline="", encoding="utf-8") as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=["id", "data_registro", "tipo_ocorrencia", "descricao", "status", "nome_declarante", "nome_autor", "deleted"])

            for dados in dados_boletim:
                id = self.next_id()
                dados['id'] = id
                dados['deleted'] = "False" 
                writer.writerow(dados)
    
    def get(self):
        with open("boletim.csv", "r", newline="", encoding="utf-8") as arquivo:
            reader = csv.DictReader(arquivo)

            for linha in reader:
                print(linha)



def main():
    db = DataBase()

    dados_boletim = [
    {
        "data_registro": "2025-11-11",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 1.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-01-08",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 2.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-06-02",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 3.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-08-17",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 4.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-06-15",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 5.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-11-03",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 6.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-11-14",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 7.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-07-28",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 8.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-01-16",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 9.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-09-10",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 10.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-10-05",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 11.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-02-02",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 12.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-05-19",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 13.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-02-12",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 14.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-05-28",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 15.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-01-27",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 16.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-11-11",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 17.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-03-16",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 18.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-03-19",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 19.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-10-11",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 20.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-07-20",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 21.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-07-18",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 22.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-09-27",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 23.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-12-25",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 24.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-03-12",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 25.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-23",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 26.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-07-17",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 27.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-12-22",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 28.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-02-06",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 29.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-08-19",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 30.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-02-14",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 31.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-07-20",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 32.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-02-23",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 33.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-05-16",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 34.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-04-15",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 35.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-04-11",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 36.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-05-11",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 37.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-06-16",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 38.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-02-17",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 39.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-02-11",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 40.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-03-16",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 41.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-02-05",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 42.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-11-24",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 43.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-05-11",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 44.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-06-10",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 45.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-05-08",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 46.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-01-26",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 47.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-07-07",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 48.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-06-04",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 49.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-02-26",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 50.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-07-02",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 51.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-06-14",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 52.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-05-14",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 53.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-12-18",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 54.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-04-12",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 55.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-08-23",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 56.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-12-07",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 57.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-07-23",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 58.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-05-12",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 59.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-01-22",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 60.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-10-24",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 61.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-06-12",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 62.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-05-08",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 63.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-01-15",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 64.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-05-13",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 65.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-07-01",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 66.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-07-19",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 67.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-08-16",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 68.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-02-04",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 69.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-09-18",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 70.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-09-22",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 71.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-03-14",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 72.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-08-26",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 73.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-11-06",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 74.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-08-02",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 75.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-10-27",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 76.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-11-01",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 77.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-09-28",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 78.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-03-07",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 79.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-09-11",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 80.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-08-04",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 81.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-06-05",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 82.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-07-02",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 83.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-04-03",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 84.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-05-09",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 85.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-03-21",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 86.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-12-09",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 87.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-03-03",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 88.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-08-03",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 89.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-05-05",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 90.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-11-07",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 91.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-03-07",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 92.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-04-13",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 93.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-06-20",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 94.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-08-15",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 95.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-12-25",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 96.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-08-11",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 97.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-02-24",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 98.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-02-11",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 99.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-06-13",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 100.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-10-27",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 101.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-10-22",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 102.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-03-12",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 103.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-12-02",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 104.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-08-27",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 105.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-12-19",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 106.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-11-14",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 107.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-05-02",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 108.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-03-21",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 109.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-07-17",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 110.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-06-25",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 111.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-24",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 112.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-12-19",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 113.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-05-25",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 114.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-05-08",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 115.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-12-26",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 116.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-01-16",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 117.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-07-25",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 118.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-12-23",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 119.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-09-06",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 120.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-09-28",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 121.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-03-27",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 122.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-07-06",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 123.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-11-20",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 124.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-12-17",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 125.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-06-22",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 126.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-03-27",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 127.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-05-27",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 128.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-05-21",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 129.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-11-21",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 130.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-10-09",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 131.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-06-02",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 132.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-06-16",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 133.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-10-12",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 134.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-09-02",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 135.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-12-03",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 136.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-03-07",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 137.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-10-05",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 138.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-02-01",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 139.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-10-12",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 140.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-03-08",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 141.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-12-14",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 142.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-01-16",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 143.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-06-14",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 144.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-08-15",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 145.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-01-08",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 146.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-02-07",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 147.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-07-06",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 148.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-09-09",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 149.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-12-20",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 150.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-11-28",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 151.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-12-14",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 152.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-01-26",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 153.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-01-28",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 154.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-05-13",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 155.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-04-17",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 156.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-06-04",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 157.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-10-24",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 158.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-04-01",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 159.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-10-07",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 160.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-09-02",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 161.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-10-15",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 162.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-15",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 163.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-10-17",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 164.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-10-01",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 165.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-04-23",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 166.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-10-24",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 167.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-07-05",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 168.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-11-06",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 169.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-11-14",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 170.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-12-16",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 171.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-05-26",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 172.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-12-08",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 173.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-05-28",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 174.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-05-04",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 175.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-02-16",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 176.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-08-18",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 177.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-05-17",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 178.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-11-19",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 179.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-08-21",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 180.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-02-15",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 181.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-04-17",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 182.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-03-24",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 183.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-10-27",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 184.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-03-03",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 185.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-06-09",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 186.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-10-01",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 187.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-10-18",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 188.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-05-22",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 189.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-04-20",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 190.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-12-06",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 191.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-01-27",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 192.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-01-27",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 193.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-08-19",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 194.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-04-23",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 195.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-11-04",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 196.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-12-01",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 197.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-06-07",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 198.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-03-06",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 199.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-05-20",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 200.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-12-24",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 201.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-08-10",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 202.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-04-16",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 203.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-08-17",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 204.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-08-23",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 205.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-12-04",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 206.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-10-23",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 207.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-11-11",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 208.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-25",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 209.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-26",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 210.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-10-01",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 211.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-08-26",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 212.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-03-12",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 213.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-05-09",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 214.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-12-16",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 215.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-06-26",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 216.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-02-15",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 217.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-05-27",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 218.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-10-01",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 219.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-03-18",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 220.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-10-26",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 221.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-03-25",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 222.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-01-03",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 223.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-08-05",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 224.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-08-26",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 225.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-01-23",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 226.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-08-14",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 227.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-01-20",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 228.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-01-03",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 229.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-01-05",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 230.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-01-26",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 231.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-02-05",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 232.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-05-04",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 233.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-05-04",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 234.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-09-18",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 235.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-12-22",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 236.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-04-13",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 237.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-01-14",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 238.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-11-01",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 239.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-01-27",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 240.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-03-20",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 241.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-04-20",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 242.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-05-23",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 243.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-06-02",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 244.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-01-20",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 245.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-02-23",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 246.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-06-07",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 247.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-01-23",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 248.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-03-19",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 249.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-11-25",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 250.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-09-06",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 251.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-08-17",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 252.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-10-05",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 253.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-11-07",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 254.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-08-08",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 255.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-05-24",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 256.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-02-08",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 257.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-03-13",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 258.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-03-05",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 259.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-25",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 260.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-12",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 261.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-11-10",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 262.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-12-26",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 263.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-10-21",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 264.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-09-08",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 265.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-12-03",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 266.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-07-28",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 267.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-07-16",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 268.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-08-25",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 269.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-12-27",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 270.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-10-18",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 271.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-04-22",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 272.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-11-02",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 273.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-05-02",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 274.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-05-11",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 275.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-07-14",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 276.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-08-15",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 277.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-10-07",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 278.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-10-09",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 279.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-12-01",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 280.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-08-11",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 281.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-10-08",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 282.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-09-17",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 283.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-02-19",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 284.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-03-27",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 285.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-09-28",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 286.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-07-06",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 287.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-09-25",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 288.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-07-07",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 289.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-06-09",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 290.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-03-15",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 291.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-12-02",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 292.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-03-16",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 293.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-08-05",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 294.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-04-20",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 295.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-07-27",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 296.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-05-03",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 297.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-07-03",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 298.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-07-09",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 299.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-06-22",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 300.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-11-26",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 301.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-01-02",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 302.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-06-25",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 303.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-12-08",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 304.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-08-13",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 305.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-06-06",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 306.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-05-20",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 307.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-12-14",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 308.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-12-14",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 309.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-03-19",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 310.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-12-14",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 311.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-11-18",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 312.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-06-28",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 313.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-05-26",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 314.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-12-07",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 315.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-11-18",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 316.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-01-14",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 317.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-11-07",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 318.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-06-27",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 319.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-12-06",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 320.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-03-17",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 321.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-03-04",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 322.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-03-02",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 323.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-06-27",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 324.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-01-20",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 325.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-07-07",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 326.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-04-22",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 327.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-11-04",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 328.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-08-09",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 329.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-01-17",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 330.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-05-01",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 331.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-11-17",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 332.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-01-24",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 333.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-06-02",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 334.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-08-14",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 335.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-07-13",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 336.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-05-21",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 337.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-03-28",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 338.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-04-21",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 339.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-07-19",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 340.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-20",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 341.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-11-16",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 342.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-05-28",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 343.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-07-11",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 344.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-08-22",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 345.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-06-08",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 346.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-07-25",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 347.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-08-01",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 348.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-03-25",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 349.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-02-08",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 350.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-07-24",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 351.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-01-01",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 352.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-04-27",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 353.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-08-25",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 354.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-04",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 355.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-04-22",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 356.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-07-26",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 357.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-08-12",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 358.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-02-24",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 359.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-12-25",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 360.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-10-01",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 361.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-02-21",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 362.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-11-04",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 363.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-01-09",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 364.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-05-09",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 365.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-07-20",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 366.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-09-05",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 367.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-11-20",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 368.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-02-10",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 369.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-11-07",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 370.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-06-23",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 371.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-02-18",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 372.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-10-18",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 373.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-10-11",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 374.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-10-23",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 375.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-06-05",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 376.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-09-13",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 377.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-07-24",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 378.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-06-11",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 379.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-06-24",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 380.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-07-04",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 381.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-12-27",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 382.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-07-21",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 383.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-09-24",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 384.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-03-11",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 385.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-04-23",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 386.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-11-28",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 387.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-10-25",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 388.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-06-04",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 389.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-04-19",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 390.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-10-15",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 391.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-08-05",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 392.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-07-28",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 393.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-08-23",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 394.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-12-27",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 395.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-02-22",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 396.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-12-16",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 397.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-03-21",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 398.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-05-20",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 399.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-11-17",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 400.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-02-02",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 401.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-03-01",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 402.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-10-17",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 403.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-01-12",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 404.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-01-24",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 405.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-11-26",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 406.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-02-03",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 407.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-01-20",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 408.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-01-08",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 409.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-10",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 410.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-06-22",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 411.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-08-09",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 412.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-02-21",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 413.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-02-10",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 414.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-09-02",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 415.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-09-11",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 416.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-01-04",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 417.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-12-22",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 418.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-09-26",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 419.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-06-01",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 420.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-01-09",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 421.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-08-20",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 422.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-03-21",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 423.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-12-26",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 424.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-09-13",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 425.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-01-04",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 426.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-10-17",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 427.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-12-05",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 428.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-03-13",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 429.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-03-08",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 430.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-01-05",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 431.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-07-08",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 432.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-06-14",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 433.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-11-20",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 434.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-04-01",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 435.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-08-10",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 436.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-02-07",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 437.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-11-14",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 438.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-03-19",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 439.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-09-14",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 440.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-05-21",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 441.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-11-20",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 442.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-03-05",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 443.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-10-04",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 444.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-03-18",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 445.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-02-20",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 446.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-05-10",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 447.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-04-06",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 448.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-02-17",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 449.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-06-19",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 450.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-03-04",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 451.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-09-22",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 452.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-04-04",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 453.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-09-11",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 454.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-07-12",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 455.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-10-16",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 456.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-07-15",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 457.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-01-11",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 458.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-06-28",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 459.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-03-21",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 460.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-05-19",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 461.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-07-16",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 462.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-11-26",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 463.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-09-18",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 464.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-11-28",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 465.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-12-11",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 466.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-12-25",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 467.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-09-08",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 468.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-05-07",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 469.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-07-05",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 470.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-03-05",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 471.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-09-01",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 472.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-08-06",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 473.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-09-28",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 474.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-12-13",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 475.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-27",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 476.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-10-11",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 477.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-08-27",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 478.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-10-01",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 479.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-11-14",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 480.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-08-14",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 481.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-11-16",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 482.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-06-12",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 483.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-01-14",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 484.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-12-16",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 485.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-05-25",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 486.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-07-08",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 487.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-09-07",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 488.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-11-11",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 489.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-04-03",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 490.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-09-17",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 491.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-04-11",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 492.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-11-10",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 493.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-03-19",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 494.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-04-11",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 495.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-10-28",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 496.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-05-27",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 497.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-10-08",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 498.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-05-10",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 499.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-04-20",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 500.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-11-20",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 501.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-07-02",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 502.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-08-17",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 503.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-05-23",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 504.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-08-26",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 505.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-04-08",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 506.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-09-23",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 507.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-01-22",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 508.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-12-18",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 509.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-01-23",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 510.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-09-18",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 511.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-10-22",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 512.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-12-18",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 513.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-04-18",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 514.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-12-15",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 515.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-06-04",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 516.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-08-16",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 517.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-05-01",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 518.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-12-13",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 519.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-09-20",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 520.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-11-18",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 521.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-09-26",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 522.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-02-09",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 523.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-04-04",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 524.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-05-27",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 525.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-11-07",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 526.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-11-15",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 527.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-09-10",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 528.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-07-05",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 529.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-04-10",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 530.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-10-10",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 531.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-10-12",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 532.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-04-19",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 533.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-07-12",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 534.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-12-26",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 535.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-09-17",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 536.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-07-26",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 537.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-04-14",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 538.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-09-21",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 539.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-05-13",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 540.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-05-20",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 541.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-12-17",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 542.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-03-19",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 543.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-01-10",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 544.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-01-10",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 545.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-24",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 546.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-03-09",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 547.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-09-18",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 548.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-12-01",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 549.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-10-22",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 550.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-06-03",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 551.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-07-08",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 552.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-12-18",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 553.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-12-18",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 554.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-09-27",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 555.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-12-08",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 556.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-12-20",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 557.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-12-16",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 558.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-06-20",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 559.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-05-19",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 560.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-06-04",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 561.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-02-16",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 562.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-07-25",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 563.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-06-26",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 564.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-01-16",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 565.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-08-14",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 566.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-06-27",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 567.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-11-18",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 568.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-10-28",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 569.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-01-26",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 570.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-02-07",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 571.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-01-23",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 572.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-03-03",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 573.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-07-03",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 574.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-11-09",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 575.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-08-14",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 576.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-04-21",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 577.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-09-17",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 578.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-07-23",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 579.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-10-25",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 580.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-09-16",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 581.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-08-05",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 582.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-05-26",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 583.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-04-12",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 584.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-07-08",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 585.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-10-13",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 586.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-06-12",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 587.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-06-07",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 588.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-02-21",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 589.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-11-23",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 590.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-12-10",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 591.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-02-28",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 592.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-08-18",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 593.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-09-06",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 594.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-12-05",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 595.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-01-28",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 596.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-09-28",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 597.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-03-04",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 598.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-09-07",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 599.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-05-16",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 600.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-10-04",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 601.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-07-28",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 602.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-09-16",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 603.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-01-15",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 604.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-04-26",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 605.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-10-25",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 606.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-03-27",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 607.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-28",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 608.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-05-22",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 609.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-03-27",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 610.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-01-09",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 611.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-06-10",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 612.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-10-25",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 613.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-07-21",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 614.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-03-19",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 615.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-11-19",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 616.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-10-21",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 617.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-12-26",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 618.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-02-14",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 619.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-06-17",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 620.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-02-24",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 621.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-05-25",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 622.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-09-02",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 623.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-05-09",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 624.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-05-25",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 625.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-06-01",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 626.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-11-02",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 627.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-05-10",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 628.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-02-12",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 629.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-02-24",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 630.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-09-08",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 631.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-05-02",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 632.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-12-23",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 633.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-08-11",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 634.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-03-12",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 635.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-10-17",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 636.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-03-19",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 637.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-08-22",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 638.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-07-10",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 639.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-08-06",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 640.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-05-20",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 641.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-09-16",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 642.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-12-18",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 643.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-09-14",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 644.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-08-03",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 645.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-07-12",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 646.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-12-03",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 647.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-03-25",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 648.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-07-26",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 649.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-07-17",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 650.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-11-09",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 651.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-05-08",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 652.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-12-19",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 653.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-03-01",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 654.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-09-26",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 655.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-08-09",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 656.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-06-25",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 657.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-11-16",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 658.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-05-18",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 659.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-04-01",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 660.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-05-22",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 661.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-07-01",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 662.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-11-12",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 663.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-12-02",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 664.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-10-23",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 665.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-05-28",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 666.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-06-25",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 667.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-05-03",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 668.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-02-19",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 669.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-04-18",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 670.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-11-16",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 671.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-12-18",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 672.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-08-23",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 673.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-11",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 674.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-08-07",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 675.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-12-03",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 676.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-10-19",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 677.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-07-13",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 678.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-08-27",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 679.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-10-05",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 680.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-03-13",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 681.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-04-05",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 682.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-06-08",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 683.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-12-21",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 684.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-10-20",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 685.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-09-16",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 686.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-08-06",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 687.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-01-26",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 688.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-03-11",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 689.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-02-27",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 690.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-06-27",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 691.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-09-24",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 692.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-12-08",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 693.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-08-02",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 694.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-02-07",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 695.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-01-08",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 696.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-02-10",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 697.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-01-11",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 698.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-02-04",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 699.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-05-18",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 700.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-11-19",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 701.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-12-17",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 702.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-10-11",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 703.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-12-10",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 704.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-03-27",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 705.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-08-14",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 706.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-12-08",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 707.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-06-08",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 708.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-09-14",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 709.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-02-22",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 710.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-05-05",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 711.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-09-18",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 712.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-05-27",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 713.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-10-05",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 714.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-12-27",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 715.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-04-26",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 716.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-06-21",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 717.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-04-21",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 718.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-12-15",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 719.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-06-10",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 720.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-06-25",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 721.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-03-17",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 722.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-01-13",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 723.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-07-19",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 724.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-02-08",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 725.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-10-11",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 726.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-03-12",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 727.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-12",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 728.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-08-12",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 729.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-01-01",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 730.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-09-03",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 731.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-09-08",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 732.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-10-10",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 733.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-03-24",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 734.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-02-02",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 735.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-06-03",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 736.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-02-19",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 737.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-05-25",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 738.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-05-17",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 739.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-10-20",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 740.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-07-04",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 741.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-05-02",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 742.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-06-26",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 743.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-03-28",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 744.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-08-23",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 745.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-03-24",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 746.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-02-01",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 747.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-06-04",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 748.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-02-22",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 749.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-07-19",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 750.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-12-27",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 751.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-11-01",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 752.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-05-14",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 753.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-12-21",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 754.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-08-06",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 755.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-11-27",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 756.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-09-16",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 757.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-12-02",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 758.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-08-16",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 759.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-05-10",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 760.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-11-11",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 761.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-06-24",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 762.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-11-16",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 763.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-07-05",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 764.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-02-07",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 765.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-04-02",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 766.",
        "status": "Em análise",
        "nome_declarante": "Ana",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-10-19",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 767.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-01-27",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 768.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-02-26",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 769.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-10-06",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 770.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-07-05",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 771.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-05-20",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 772.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-07-03",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 773.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-07-07",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 774.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-12-05",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 775.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-12-12",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 776.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-09-19",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 777.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-02-06",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 778.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-08-22",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 779.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-07-15",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 780.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-07-03",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 781.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-04-16",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 782.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-06-03",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 783.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-05-16",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 784.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-04-11",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 785.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-03-12",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 786.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-05-08",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 787.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-05-20",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 788.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-07-07",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 789.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-10-21",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 790.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-07-16",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 791.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-07-02",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 792.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-01-12",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 793.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-03-04",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 794.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-10-08",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 795.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-11-07",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 796.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-06-23",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 797.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-01-09",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 798.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-08-26",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 799.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-10-12",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 800.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-11-15",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 801.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-03-09",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 802.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-08-24",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 803.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-04-24",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 804.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-10-15",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 805.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-10-17",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 806.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-06-12",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 807.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-06-03",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 808.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-04-12",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 809.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-11-14",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 810.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-07-09",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 811.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-01-05",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 812.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-12-18",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 813.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-03-16",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 814.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-11-05",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 815.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-09-12",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 816.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-01-19",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 817.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-02-22",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 818.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-03-12",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 819.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-12-05",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 820.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-11-11",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 821.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-12-09",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 822.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-10-10",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 823.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-04-14",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 824.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-09-28",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 825.",
        "status": "Em análise",
        "nome_declarante": "Pedro",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-07-02",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 826.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-04-28",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 827.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-11-16",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 828.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-06-07",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 829.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-01-12",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 830.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-03-24",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 831.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-05-11",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 832.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-04-15",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 833.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-03-28",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 834.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-07-27",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 835.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-05-10",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 836.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-12-13",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 837.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-11-11",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 838.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-04-01",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 839.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-07-01",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 840.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-08-28",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 841.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-11-25",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 842.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-03-05",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 843.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-04-23",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 844.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-01-28",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 845.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-12-28",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 846.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-11-27",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 847.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-03-17",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 848.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-07-05",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 849.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-03-25",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 850.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-04-10",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 851.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-02-07",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 852.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-05-17",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 853.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-10-10",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 854.",
        "status": "Concluído",
        "nome_declarante": "Camila",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-11-09",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 855.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-11-07",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 856.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-03-17",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 857.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-08-27",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 858.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-05-22",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 859.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-02-23",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 860.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-04-22",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 861.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-12-25",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 862.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-01-01",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 863.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-08-08",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 864.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-01-11",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 865.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-07-17",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 866.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-05-27",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 867.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-01-18",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 868.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-03-24",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 869.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-02-02",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 870.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-04-07",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 871.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-01-17",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 872.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-10-05",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 873.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-04-12",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 874.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-06-26",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 875.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-09-12",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 876.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-03-07",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 877.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-06-06",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 878.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-04-16",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 879.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-07-06",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 880.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-12-17",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 881.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-03-26",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 882.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-07-25",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 883.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-10-09",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 884.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-12-28",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 885.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-10-28",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 886.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-11-22",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 887.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-07-09",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 888.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-05-27",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 889.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-08-14",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 890.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-09-25",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 891.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-12-24",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 892.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-08-03",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 893.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-12-01",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 894.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-01-20",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 895.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-02-12",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 896.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-07-01",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 897.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-12-22",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 898.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-03-26",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 899.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-06-08",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 900.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-03-20",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 901.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-07-19",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 902.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-11-06",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 903.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-11-27",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 904.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-09-07",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 905.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-11-13",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 906.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-05-10",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 907.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-07-17",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 908.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-11-07",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 909.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-12-04",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 910.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-10-08",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 911.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-08-23",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 912.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-01-25",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 913.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-12-16",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 914.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-01-18",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 915.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-05-09",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 916.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-11-21",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 917.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-08-23",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 918.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-07-12",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 919.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-04-17",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 920.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-07-02",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 921.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-10-19",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 922.",
        "status": "Arquivado",
        "nome_declarante": "Camila",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-08-03",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 923.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-03-17",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 924.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-10-18",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 925.",
        "status": "Pendente",
        "nome_declarante": "Carlos",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-09-17",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 926.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-04-19",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 927.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-03-26",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 928.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-11-09",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 929.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-01-23",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 930.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-01-05",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 931.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-02-17",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 932.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-07-04",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 933.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-08-01",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 934.",
        "status": "Concluído",
        "nome_declarante": "Issllany",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-02",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 935.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-11-07",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 936.",
        "status": "Arquivado",
        "nome_declarante": "Fernanda",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-01-25",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 937.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-02-16",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 938.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-08-17",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 939.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-06-07",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 940.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-07-10",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 941.",
        "status": "Em análise",
        "nome_declarante": "Maria",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-11-10",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 942.",
        "status": "Concluído",
        "nome_declarante": "Ana",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-06-26",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 943.",
        "status": "Concluído",
        "nome_declarante": "Maria",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-01-25",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 944.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-11-08",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 945.",
        "status": "Em análise",
        "nome_declarante": "Julio",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-04-08",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 946.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-11-11",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 947.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-12-03",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 948.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-12-23",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 949.",
        "status": "Concluído",
        "nome_declarante": "Julio",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-05-21",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 950.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-05-28",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 951.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-04-16",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 952.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-06-09",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 953.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-03-01",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 954.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-07-19",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 955.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-04-01",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 956.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-01-13",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 957.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-08-23",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 958.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-09-19",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 959.",
        "status": "Em análise",
        "nome_declarante": "Camila",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-08-10",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 960.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-02-20",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 961.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-11-12",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 962.",
        "status": "Pendente",
        "nome_declarante": "Ana",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-05-15",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 963.",
        "status": "Pendente",
        "nome_declarante": "Lucas",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-10-24",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 964.",
        "status": "Arquivado",
        "nome_declarante": "Pedro",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-06-18",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 965.",
        "status": "Pendente",
        "nome_declarante": "Pedro",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-11-11",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 966.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-10-04",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 967.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-01-25",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 968.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-06-05",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 969.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-06-09",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 970.",
        "status": "Arquivado",
        "nome_declarante": "Ana",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-09-17",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 971.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-09-04",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 972.",
        "status": "Pendente",
        "nome_declarante": "Fernanda",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-06-09",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 973.",
        "status": "Em análise",
        "nome_declarante": "João",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-01-06",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 974.",
        "status": "Arquivado",
        "nome_declarante": "Julio",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-05-20",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 975.",
        "status": "Em análise",
        "nome_declarante": "Lucas",
        "nome_autor": "Camila"
    },
    {
        "data_registro": "2025-10-06",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 976.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Julio"
    },
    {
        "data_registro": "2025-05-26",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 977.",
        "status": "Pendente",
        "nome_declarante": "João",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-11-21",
        "tipo_ocorrencia": "Fraude",
        "descricao": "Descrição da ocorrência número 978.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-02-19",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 979.",
        "status": "Pendente",
        "nome_declarante": "Maria",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-03-06",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 980.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-05-27",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 981.",
        "status": "Pendente",
        "nome_declarante": "Issllany",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-05-26",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 982.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-11-24",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 983.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-03-04",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 984.",
        "status": "Arquivado",
        "nome_declarante": "Maria",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-03-16",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 985.",
        "status": "Em análise",
        "nome_declarante": "Fernanda",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-08-19",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 986.",
        "status": "Em análise",
        "nome_declarante": "Carlos",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-09-17",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 987.",
        "status": "Em análise",
        "nome_declarante": "Issllany",
        "nome_autor": "Ana"
    },
    {
        "data_registro": "2025-02-27",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 988.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-11-09",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 989.",
        "status": "Arquivado",
        "nome_declarante": "João",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-12-19",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 990.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "Pedro"
    },
    {
        "data_registro": "2025-06-28",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 991.",
        "status": "Arquivado",
        "nome_declarante": "Lucas",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-02-20",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 992.",
        "status": "Pendente",
        "nome_declarante": "Camila",
        "nome_autor": "Maria"
    },
    {
        "data_registro": "2025-10-11",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 993.",
        "status": "Concluído",
        "nome_declarante": "João",
        "nome_autor": "Fernanda"
    },
    {
        "data_registro": "2025-12-09",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 994.",
        "status": "Arquivado",
        "nome_declarante": "Issllany",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-02-06",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 995.",
        "status": "Concluído",
        "nome_declarante": "Carlos",
        "nome_autor": "Issllany"
    },
    {
        "data_registro": "2025-03-25",
        "tipo_ocorrencia": "Furto",
        "descricao": "Descrição da ocorrência número 996.",
        "status": "Arquivado",
        "nome_declarante": "Carlos",
        "nome_autor": "Lucas"
    },
    {
        "data_registro": "2025-06-13",
        "tipo_ocorrencia": "Agressão",
        "descricao": "Descrição da ocorrência número 997.",
        "status": "Concluído",
        "nome_declarante": "Pedro",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-09-04",
        "tipo_ocorrencia": "Roubo",
        "descricao": "Descrição da ocorrência número 998.",
        "status": "Concluído",
        "nome_declarante": "Fernanda",
        "nome_autor": "Carlos"
    },
    {
        "data_registro": "2025-02-28",
        "tipo_ocorrencia": "Acidente",
        "descricao": "Descrição da ocorrência número 999.",
        "status": "Concluído",
        "nome_declarante": "Lucas",
        "nome_autor": "João"
    },
    {
        "data_registro": "2025-01-17",
        "tipo_ocorrencia": "Vandalismo",
        "descricao": "Descrição da ocorrência número 1000.",
        "status": "Pendente",
        "nome_declarante": "Julio",
        "nome_autor": "Carlos"
    }
]

    db.insert(dados_boletim)
    db.get()

main()
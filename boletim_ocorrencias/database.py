import csv, json, os

class DataBase:

##CRIACAO DO BANCO DADOS
    def __init__(self):
        if os.path.exists("boletim.csv") and os.path.exists("boletim.seq"):
            pass
        else:
            with open("boletim.csv", "w", newline="", encoding="utf-8") as arquivo:
                writer = csv.DictWriter(arquivo, fieldnames=["id", "data_registro", "tipo_ocorrencia", "descricao", "status", "nome_declarante", "nome_autor", "deleted"])
                writer.writeheader()    
            with open("boletim.seq", "w") as arquivo:
                arquivo.write('0')

          


##VERIFICAO DO ID
    def next_id(self):
        with open("boletim.seq", "r+") as arquivo:
            prev_id = int(arquivo.readline())
            next_id = prev_id + 1
            arquivo.seek(0)
            arquivo.write(str(next_id))
        return prev_id


##INSERIR NOVO ID
    def insert(self, registro_boletim):
        with open("boletim.csv", "a", newline="", encoding="utf-8") as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=["id", "data_registro", "tipo_ocorrencia", "descricao", "status", "nome_declarante", "nome_autor", "deleted"])

            for registro in registro_boletim:
                id = self.next_id()
                registro['id'] = id
                registro['deleted'] = False 
                writer.writerow(registro)
    

##RETORNAR OS REGISTROS
    def get(self):
        registros = []
        with open("boletim.csv", "r", newline="", encoding="utf-8") as arquivo:
            reader = csv.DictReader(arquivo)
            for linha in reader:
                if linha["deleted"] == "False":
                    registros.append(linha)

        return registros


##ATUALIZAR OS REGISTROS
    def update(self, id, novos_registro):
        registro = []
        with open("boletim.csv", "r", newline="", encoding="utf-8") as arquivo:
            reader = csv.DictReader(arquivo)
            registro = list(reader)

        
        atualizado = False
        for linha in registro:
            if linha['id'] == str(id):
                linha.update(novos_registro)
                atualizado = True
                break

        if atualizado:
            with open("boletim.csv", "w", newline="", encoding="utf-8") as arquivo:
                arquivo = csv.DictWriter(arquivo, fieldnames=["id", "data_registro", "tipo_ocorrencia", "descricao", "status", "nome_declarante", "nome_autor", "deleted"])
                arquivo.writeheader()  
                arquivo.writerows(registro)
                print(f"ID {id} atualizado com sucesso!")
        else:
            print("ID não encontrado!")
    

## DELETAR LOGICAMENTE OS REGISTROS

    def delete(self, id):
        registro = []
        with open("boletim.csv", "r", newline="", encoding="utf-8") as arquivo:
            reader = csv.DictReader(arquivo)
            registro = list(reader)

        
        deletado = False
        for linha in registro:
            if linha['id'] == str(id):
                linha["deleted"] = True
                deletado = True
                break

        if deletado:
            with open("boletim.csv", "w", newline="", encoding="utf-8") as arquivo:
                arquivo = csv.DictWriter(arquivo, fieldnames=["id", "data_registro", "tipo_ocorrencia", "descricao", "status", "nome_declarante", "nome_autor", "deleted"])
                arquivo.writeheader()  
                arquivo.writerows(registro)
                print(f"ID {id} deletado com sucesso!")
        else:
            print("ID não encontrado!")

## CONTAR OS REGISTROS 

    def count(self):
            with open("boletim.csv", "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for line in reader:
                    return sum(1 for linha in reader if linha["deleted"] == "False")
                
## VACUUM

    def vacuum(self):
        registros = []
        with open("boletim.csv", "r", newline="", encoding="utf-8") as arquivo:
            reader = csv.DictReader(arquivo)
            registros = list(reader)
        linhas_validas = []
        for linhas in registros:
            if linhas["deleted"] == "False":
                linhas_validas.append(linhas) 
        with open("boletim.csv", "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=["id", "data_registro", "tipo_ocorrencia", "descricao", "status", "nome_declarante", "nome_autor", "deleted"])
            writer.writeheader()
            writer.writerows(linhas_validas)

def main():
    db = DataBase()
    with open("registros_exemplo.json", "r", encoding="utf-8") as arquivo:
        registros = json.load(arquivo)
    


main()
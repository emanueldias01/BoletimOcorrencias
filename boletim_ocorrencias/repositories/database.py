import csv, json, os

class DataBase:

##CRIACAO DO BANCO DADOS
    def __init__(self):
        base_path = os.path.join(os.path.dirname(__file__), "../../data")
        os.makedirs(base_path, exist_ok=True)

        self.csv_path = os.path.join(base_path, "boletim.csv")
        self.seq_path = os.path.join(base_path, "boletim.seq")
        
        if not os.path.exists(self.csv_path):
            with open(self.csv_path, "w", newline="", encoding="utf-8") as arquivo:
                escritor = csv.DictWriter(
                    arquivo,
                    fieldnames=["id", "data_registro", "tipo_ocorrencia", "descricao", "status", "nome_declarante", "nome_autor", "deleted"]
                )
                escritor.writeheader()

        if not os.path.exists(self.seq_path):
            with open(self.seq_path, "w", encoding="utf-8") as arquivo:
                arquivo.write("0")
          

##VERIFICAO DO ID
    def next_id(self):
        with open(self.seq_path, "r+") as arquivo:
            conteudo = arquivo.readline().strip()
            prev_id = int(conteudo) if conteudo else 0
            next_id = prev_id + 1
            arquivo.seek(0)
            arquivo.write(str(next_id))
        return prev_id


##INSERIR NOVO ID
    def insert(self, registro_boletim):
        with open(self.csv_path, "a", newline="", encoding="utf-8") as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=["id", "data_registro", "tipo_ocorrencia", "descricao", "status", "nome_declarante", "nome_autor", "deleted"])

            for registro in registro_boletim:
                id = self.next_id()
                registro['id'] = id
                registro['deleted'] = "False"  
                writer.writerow(registro)
    

##RETORNAR OS REGISTROS
    def get(self):
        registros = []
        with open(self.csv_path, "r", newline="", encoding="utf-8") as arquivo:
            reader = csv.DictReader(arquivo)
            for linha in reader:
                if linha["deleted"] == "False":
                    registros.append(linha)

        return registros


##ATUALIZAR OS REGISTROS

    def update(self, id, novos_registro):
        updated = False
        tmp_path = self.csv_path + ".tmp"

        with open(self.csv_path, "r", newline="", encoding="utf-8") as arquivo_orig, \
            open(tmp_path, "w", newline="", encoding="utf-8") as arquivo_temp:
            reader = csv.DictReader(arquivo_orig)
            writer = csv.DictWriter(arquivo_temp, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                if row['id'].strip() == str(id):
                    row.update(novos_registro)
                    updated = True
                    print(f"ID {id} atualizado com sucesso!")
                writer.writerow(row)
        
        os.replace(tmp_path, self.csv_path)

        if not updated:
            print("ID não encontrado!")
        

    

## DELETAR LOGICAMENTE OS REGISTROS

    def delete(self, id):
        deleted = False
        tmp_path = self.csv_path + ".tmp"

        with open(self.csv_path, "r", newline="", encoding="utf-8") as arquivo_orig, \
            open(tmp_path, "w", newline="", encoding="utf-8") as arquivo_temp:
            reader = csv.DictReader(arquivo_orig)
            writer = csv.DictWriter(arquivo_temp, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                if row['id'].strip() == str(id):
                    row["deleted"] = "True"
                    deleted = True
                    print(f"ID {id} deletado com sucesso!")
                writer.writerow(row)
        
        os.replace(tmp_path, self.csv_path)

        if not deleted:
            print("ID não encontrado!")

## CONTAR OS REGISTROS 

    def count(self):
            with open(self.csv_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for line in reader:
                    return sum(1 for linha in reader if linha["deleted"] == "False")
                
## VACUUM

    def vacuum(self):
        tmp_path = self.csv_path + ".tmp"

        with open(self.csv_path, "r", newline="", encoding="utf-8") as arquivo_orig, \
            open(tmp_path, "w", newline="", encoding="utf-8") as arquivo_temp:
            reader = csv.DictReader(arquivo_orig)
            writer = csv.DictWriter(arquivo_temp, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                if row["deleted"]=="False":
                    writer.writerow(row)
        
        os.replace(tmp_path, self.csv_path)


def main():
    db = DataBase()

main()
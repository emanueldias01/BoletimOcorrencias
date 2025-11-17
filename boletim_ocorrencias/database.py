import csv, os
import io
import zipfile
from fastapi.responses import StreamingResponse


class DataBase:

##CRIACAO DO BANCO DADOS
    def __init__(self):
        self.base_path = os.path.join(os.path.dirname(__file__), "./data")
        
        self.csv_path = os.path.join(self.base_path, "boletim.csv")
        self.seq_path = os.path.join(self.base_path, "boletim.seq")
          

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
    

##RETORNAR OS REGISTROS (PAGINADOS)
    def get(self, num_pagina: int, tam_pagina: int):
        inicio = (num_pagina - 1) * tam_pagina
        fim = inicio + tam_pagina

        registros = []
        total_registros = 0

        with open(self.csv_path, "r", newline="", encoding="utf-8") as arquivo:
            reader = csv.DictReader(arquivo)
            for _, linha in enumerate(reader):
                if linha["deleted"] == "False":
                    total_registros += 1
                    if total_registros > inicio and total_registros <= fim:
                        registros.append(linha)

        return registros
    


##ATUALIZAR OS REGISTROS

    def update(self, id, novos_registro) -> bool:
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
            return False
        else: 
            return True


    

## DELETAR LOGICAMENTE OS REGISTROS

    def delete(self, id) -> bool:
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
            return False
        else:
            return True

## CONTAR OS REGISTROS 

    def count(self):
            with open(self.csv_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
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

    def get_zip(self):

        if not os.path.exists(self.csv_path):
            return {"erro": "Arquivo CSV não encontrado."}

        def stream_zip():
            buffer = io.BytesIO()

            #cria zip no buffer
            with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
                #add o csv no zip
                zipf.write(self.csv_path, arcname="boletim.csv")

            #ponteiro no comeco
            buffer.seek(0)

            chunk_size = 1024 * 1024  #1mb por vez
            while chunk := buffer.read(chunk_size):
                yield chunk

        return StreamingResponse(
            stream_zip(),
            media_type="application/zip",
            headers={"Content-Disposition": "attachment; filename=boletim.zip"}
        )


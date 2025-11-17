# BoletimOcorrencias

## Como rodar o projeto
 - clone o repositorio
 - crie um ambiente virtual chamado ".venv"
    ```bash
    python -m venv .venv
    ```
- entre no ambiente virtual
    ```bash
    source .venv/bin/activate
    ```
- baixe as dependências para rodar o projeto
    ```bash
    pip install -r requirements.txt
    ```
- navege para a pasta boletim_ocorrencias
- inicie o projeto
    ```bash
    fastapi dev boletim_ocorrencias/main.py
    ```
- para gerar 1000 dados fictícios
    ```bash
    python -m boletim_ocorrencias.scripts.generate_data
    ```
## IMPORTANTE
 - toda vez que baixar alguma coisa, atualize o requirements.txt
    ```bash
    pip freeze > requirements.txt
    ```


## MODELAGEM 

```mermaid
classDiagram
direction LR

class Declarante {
    id_declarante: int
    nome: str
    cpf: str
    data_nascimento: date
    endereco: str
    tipo_envolvimento: str
}

class Autor {
    id_autor: int
    nome: str
    matricula: str
    posto: str
    lotacao: str
}

class BoletimOcorrencia {
    id_boletim: int
    data_registro: date
    tipo_ocorrencia: str
    descricao: str
    status: str
    id_autor: int <<FK>>
}

class Declarante_Boletim {
    id_declarante: int <<FK>>
    id_boletim: int <<FK>>
}

Declarante --> Declarante_Boletim
BoletimOcorrencia --> Declarante_Boletim 
Autor --> BoletimOcorrencia 

```

from fastapi import APIRouter, status
from boletim_ocorrencias.schemas import *
from boletim_ocorrencias.database import DataBase
from fastapi import HTTPException
import hashlib
import pickle

router = APIRouter(
    prefix="/api/boletim",
    tags=["Boletim"]
)

banco = DataBase()

#EXEMPLOS TESTE

@router.get(
    path="/get",
    response_model=list[BoletimOcorrenciaResponse],
    status_code=status.HTTP_200_OK,
    description='busca todos os boletins registrados no banco'
)
def get_boletins(page : int=1, size : int=15):
    registros_csv = banco.get(page, size)

    boletins = []
    for line in registros_csv:
        boletins.append(
            BoletimOcorrenciaResponse(
                id=line['id'],
                data_registro=line['data_registro'],
                tipo_ocorrencia=TipoOcorrencia(line['tipo_ocorrencia']),
                descricao=line['descricao'],
                status=StatusBoletim(line['status']),
                nome_declarante=line['nome_declarante'],
                nome_autor=line['nome_autor']
                # declarante=Declarante(
                #     nome="Lucas Ferreira",
                #     cpf="123.456.789-10",
                #     data_nascimento=date(1992, 5, 17),
                #     endereco="Rua das Palmeiras, 120 - Centro, Belo Horizonte/MG",
                #     tipo_envolvimento=TipoEnvolvimento.VITIMA
                # ),
                # autor=Autor(
                #     nome="Sgt. Carlos Mendes",
                #     matricula="PMMG-45821",
                #     posto="Sargento",
                #     lotacao="7º BPM - Belo Horizonte"
                # )
            )
        )


    return boletins

@router.get(
    path="/count",
    status_code=status.HTTP_200_OK,
    description='Mostra o total de entidades existentes'
)
def count():
    return banco.count()

#@router.get(
#    path="/{id}",
#    response_model=list[BoletimOcorrenciaResponse],
#    status_code=status.HTTP_200_OK,
#    description='busca o boletim com o id passado na requisicao' 
#)

#FALTA FAZER
#def get_boletim_by_id(id : int):
#    boletim = BoletimOcorrenciaResponse(
#        id=id,
#        data_registro=date(2025, 10, 8),
#        tipo_ocorrencia=TipoOcorrencia.VIOLENCIA_DOMESTICA,
#        descricao="Relato de agressão física entre casal. A vítima acionou a polícia após ser empurrada e ameaçada verbalmente pelo companheiro.",
#        status=StatusBoletim.REGISTRADO,
#        declarante=Declarante(
#            nome="Ana Paula Souza",
#            cpf="321.987.654-99",
#            data_nascimento=date(1994, 8, 29),
#            endereco="Rua das Acácias, 55 - Jardim América, Contagem/MG",
#            tipo_envolvimento=TipoEnvolvimento.DECLARANTE
#        ),
#        autor=Autor(
#            nome="Ten. Ricardo Lima",
#            matricula="PMMG-40112",
#            posto="Tenente",
#            lotacao="2ª Cia PM - Contagem"
#        )
#    )
#
#    return boletim

@router.post(
    path="/insert",
    response_model=list[BoletimOcorrenciaBase],
    status_code=status.HTTP_201_CREATED,
    description='cria um boletim a partir dos parametros passados no corpo da requisição'
)
def create_boletim(boletins : list[BoletimOcorrenciaBase]):
    registro_inserido = []
    for boletim in boletins:
        registro = {
            "data_registro":boletim.data_registro,
            "tipo_ocorrencia":boletim.tipo_ocorrencia.value,
            "descricao":boletim.descricao,
            "status":boletim.status.value,
            "nome_declarante":boletim.nome_declarante,
            "nome_autor":boletim.nome_autor
        }
        registro_inserido.append(registro)
    
    banco.insert(registro_inserido)
    return registro_inserido

@router.put(
    path="/update",
    response_model=BoletimOcorrenciaResponse,
    status_code=status.HTTP_201_CREATED,
    description='busca o boletim que tem o id passado no corpo da requisicao e edita seus campos'
)
def update_boletim(boletim : BoletimOcorrenciaResponse):

    novo_registro = {
        "id":boletim.id,
        "data_registro":boletim.data_registro,
        "tipo_ocorrencia":boletim.tipo_ocorrencia.value,
        "descricao":boletim.descricao,
        "status":boletim.status.value,
        "nome_declarante":boletim.nome_declarante,
        "nome_autor":boletim.nome_autor
    }

    banco.update(boletim.id, novo_registro)

    return novo_registro

@router.delete(
    path="/delete/{id}",
    status_code=status.HTTP_201_CREATED,
    description='deleta o boletim com o id passado no path'
)

def delete_boletim_by_id(id : int):
    return banco.delete(id)

@router.post(
    path="/zip",
    status_code=status.HTTP_200_OK,
    description="Retorna dados compactados em streaming",
)
def get_zip():
    return banco.get_zip()

@router.post(
    path="/hash/{algoritmo}",
    status_code=status.HTTP_200_OK,
    description="retorna dados hasheados de acordo com o hash de escolha"
)
def hash_data(boletim : BoletimOcorrenciaBase, algoritmo: str):
    algoritmo = algoritmo.lower()

    if algoritmo not in ["md5", "sha1", "sha256"]:
        raise HTTPException(
            status_code=400,
            detail="Algoritmo inválido. Use MD5, SHA1 ou SHA256."
        )


    texto = boletim.json().encode("utf-8")

    if algoritmo == "md5":
        resultado = hashlib.md5(texto).hexdigest()
    elif algoritmo == "sha1":
        resultado = hashlib.sha1(texto).hexdigest()
    else:
        resultado = hashlib.sha256(texto).hexdigest()

    return {"algoritmo": algoritmo.upper(), "hash": resultado}

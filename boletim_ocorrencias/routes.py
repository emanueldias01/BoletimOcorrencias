from fastapi import APIRouter, status
from schemas import *

router = APIRouter(
    prefix="/api/boletim",
    tags=["Boletim"]
)

#EXEMPLOS TESTE

@router.get(
    path="/",
    response_model=list[BoletimOcorrenciaResponse],
    status_code=status.HTTP_200_OK,
    description='busca todos os boletins registrados no banco'
)
def get_boletins():
    boletins = [
    BoletimOcorrenciaResponse(
        id=1,
        data_registro=date(2025, 10, 1),
        tipo_ocorrencia=TipoOcorrencia.FURTO,
        descricao="Furto de celular ocorrido em uma praça pública durante a noite. A vítima relatou que o autor aproveitou um momento de distração.",
        status=StatusBoletim.EM_INVESTIGACAO,
        declarante=Declarante(
            nome="Lucas Ferreira",
            cpf="123.456.789-10",
            data_nascimento=date(1992, 5, 17),
            endereco="Rua das Palmeiras, 120 - Centro, Belo Horizonte/MG",
            tipo_envolvimento=TipoEnvolvimento.VITIMA
        ),
        autor=Autor(
            nome="Sgt. Carlos Mendes",
            matricula="PMMG-45821",
            posto="Sargento",
            lotacao="7º BPM - Belo Horizonte"
        )
    ),
    BoletimOcorrenciaResponse(
        id=2,
        data_registro=date(2025, 9, 27),
        tipo_ocorrencia=TipoOcorrencia.ACIDENTE_TRANSITO,
        descricao="Colisão entre carro e motocicleta na Avenida Brasil. O condutor do carro alegou que o motociclista avançou o sinal vermelho.",
        status=StatusBoletim.CONCLUIDO,
        declarante=Declarante(
            nome="Mariana Oliveira",
            cpf="987.654.321-00",
            data_nascimento=date(1985, 11, 2),
            endereco="Av. Brasil, 900 - Santa Efigênia, Belo Horizonte/MG",
            tipo_envolvimento=TipoEnvolvimento.CONDUTOR
        ),
        autor=Autor(
            nome="Cb. André Rocha",
            matricula="PMMG-52367",
            posto="Cabo",
            lotacao="16º BPM - Belo Horizonte"
        )
    ),
    BoletimOcorrenciaResponse(
        id=3,
        data_registro=date(2025, 10, 8),
        tipo_ocorrencia=TipoOcorrencia.VIOLENCIA_DOMESTICA,
        descricao="Relato de agressão física entre casal. A vítima acionou a polícia após ser empurrada e ameaçada verbalmente pelo companheiro.",
        status=StatusBoletim.REGISTRADO,
        declarante=Declarante(
            nome="Ana Paula Souza",
            cpf="321.987.654-99",
            data_nascimento=date(1994, 8, 29),
            endereco="Rua das Acácias, 55 - Jardim América, Contagem/MG",
            tipo_envolvimento=TipoEnvolvimento.DECLARANTE
        ),
        autor=Autor(
            nome="Ten. Ricardo Lima",
            matricula="PMMG-40112",
            posto="Tenente",
            lotacao="2ª Cia PM - Contagem"
        )
    )
]

    return boletins


@router.get(
    path="/{id}",
    response_model=list[BoletimOcorrenciaResponse],
    status_code=status.HTTP_200_OK,
    description='busca o boletim com o id passado na requisicao' 
)
def get_boletim_by_id(id : int):
    boletim = BoletimOcorrenciaResponse(
        id=id,
        data_registro=date(2025, 10, 8),
        tipo_ocorrencia=TipoOcorrencia.VIOLENCIA_DOMESTICA,
        descricao="Relato de agressão física entre casal. A vítima acionou a polícia após ser empurrada e ameaçada verbalmente pelo companheiro.",
        status=StatusBoletim.REGISTRADO,
        declarante=Declarante(
            nome="Ana Paula Souza",
            cpf="321.987.654-99",
            data_nascimento=date(1994, 8, 29),
            endereco="Rua das Acácias, 55 - Jardim América, Contagem/MG",
            tipo_envolvimento=TipoEnvolvimento.DECLARANTE
        ),
        autor=Autor(
            nome="Ten. Ricardo Lima",
            matricula="PMMG-40112",
            posto="Tenente",
            lotacao="2ª Cia PM - Contagem"
        )
    )

    return boletim

@router.post(
    path="/",
    response_model=BoletimOcorrenciaResponse,
    status_code=status.HTTP_201_CREATED,
    description='cria um boletim a partir dos parametros passados no corpo da requisição'
)
def create_boletim(boletim : BoletimOcorrenciaBase):

    return BoletimOcorrenciaResponse(
        id=1,
        data_registro=boletim.data_registro,
        tipo_ocorrencia=boletim.tipo_ocorrencia,
        descricao=boletim.descricao,
        status=boletim.status,
        declarante=boletim.declarante,
        autor=boletim.autor
    )

@router.put(
    path="/",
    response_model=BoletimOcorrenciaResponse,
    status_code=status.HTTP_201_CREATED,
    description='busca o boletim que tem o id passado no corpo da requisicao e edita seus campos'
)
def update_boletim(boletim : BoletimOcorrenciaBase):

    return BoletimOcorrenciaResponse(
        id=1,
        data_registro=boletim.data_registro,
        tipo_ocorrencia=boletim.tipo_ocorrencia,
        descricao=boletim.descricao,
        status=boletim.status,
        declarante=boletim.declarante,
        autor=boletim.autor
    )

@router.delete(
    path="/{id}",
    status_code=status.HTTP_201_CREATED,
    description='deleta o boletim com o id passado no path'
)
def delete_boletim_by_id(id : int):
    pass

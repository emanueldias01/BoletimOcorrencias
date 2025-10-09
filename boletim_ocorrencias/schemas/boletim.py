from pydantic import BaseModel
from datetime import date
from enum import Enum

class TipoOcorrencia(Enum):
    FURTO = "Furto"
    ROUBO = "Roubo"
    HOMICIDIO = "Homicídio"
    LESAO_CORPORAL = "Lesão Corporal"
    AMEACA = "Ameaça"
    VIOLENCIA_DOMESTICA = "Violência Doméstica"
    ESTELIONATO = "Estelionato"
    DANOS_MATERIAIS = "Danos Materiais"
    ACIDENTE_TRANSITO = "Acidente de Trânsito"
    EMBRIAGUEZ_AO_VOLANTE = "Embriaguez ao Volante"
    DESAPARECIMENTO_PESSOA = "Desaparecimento de Pessoa"
    ENCONTRO_CADAVER = "Encontro de Cadáver"
    ENCONTRO_PESSOA = "Encontro de Pessoa"
    PERTURBACAO_TRANQUILIDADE = "Perturbação do Sossego/Tranquilidade"
    VIOLACAO_DOMICILIO = "Violação de Domicílio"
    DANO = "Dano"
    POSSE_DROGAS = "Posse de Drogas"
    TRAFICO_DROGAS = "Tráfico de Drogas"
    PORTE_ARMA = "Porte Ilegal de Arma"
    RECEPTACAO = "Receptação"
    CRIME_CIBERNETICO = "Crime Cibernético"
    FRAUDE = "Fraude"
    DIFAMACAO = "Difamação"
    INJURIA = "Injúria"
    CALUNIA = "Calúnia"
    DESOBEDIENCIA = "Desobediência"
    DESACATO = "Desacato"
    VIOLACAO_MEDIDA_PROTETIVA = "Violação de Medida Protetiva"
    TENTATIVA_SUICIDIO = "Tentativa de Suicídio"
    MAUS_TRATOS_ANIMAIS = "Maus-tratos a Animais"
    OUTROS = "Outros"

class StatusBoletim(Enum):
    REGISTRADO = "Registrado"                  
    EM_ANALISE = "Em Análise"                 
    EM_INVESTIGACAO = "Em Investigação"        
    COMPLEMENTADO = "Complementado"            
    ENCAMINHADO = "Encaminhado"               
    SUSPENSO = "Suspenso"                      
    ARQUIVADO = "Arquivado"                    
    CONCLUIDO = "Concluído"                    
    CANCELADO = "Cancelado"                   
    AGUARDANDO_VALIDACAO = "Aguardando Validação"
    REABERTO = "Reaberto"  

class TipoEnvolvimento(Enum):
    DECLARANTE = "Declarante"              
    VITIMA = "Vítima"                      
    AUTOR = "Autor_Crime"                        
    SUSPEITO = "Suspeito"                  
    TESTEMUNHA = "Testemunha"              
    CONDUTOR = "Condutor"                  
    PASSAGEIRO = "Passageiro"              
    PEDESTRE = "Pedestre"                  
    REPRESENTANTE_LEGAL = "Representante Legal"  
    PROPRIETARIO = "Proprietário"          
    ACIONANTE = "Acionante"                
    INDICIADO = "Indiciado"                
    SOCORRISTA = "Socorrista"              
    RESPONSAVEL_ESTABELECIMENTO = "Responsável pelo Estabelecimento"
    OUTRO = "Outro"                        

class BoletimOcorrenciaCreate(BaseModel):
    data_registro : date
    tipo_ocorrencia : TipoOcorrencia
    descricao : str
    status : StatusBoletim


#Pessoa que registrou o boletim
class Declarante(BaseModel):
    nome : str
    cpf : str
    data_nascimento : date
    endereco : str
    tipo_envolvimento : TipoEnvolvimento



#Policial
class Autor(BaseModel):
    nome : str
    matricula : str
    posto : str
    lotacao : str

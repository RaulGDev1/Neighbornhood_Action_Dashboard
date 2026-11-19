
# ============================================
# NEIGHBORHOOD ACTION DASHBOARD
# Base inicial de ocorrências comunitárias
# ============================================

BAIRRO = "Jardim Esperança"

CATEGORIAS = [
    "iluminacao",
    "acessibilidade",
    "limpeza",
    "conservacao"
]

STATUS_VALIDOS = [
    "aberta",
    "em analise",
    "concluida"
]

# Dados iniciais simulados
OCORRENCIAS_INICIAIS = [
    {
        "id": "OC001",
        "categoria": "iluminacao",
        "descricao": "Poste apagado durante a noite",
        "localidade": "Rua das Flores",
        "abertura_dia": 2,
        "status": "aberta",
        "conclusao_dia": None
    },
    {
        "id": "OC002",
        "categoria": "limpeza",
        "descricao": "Acumulo de lixo na calcada",
        "localidade": "Praca Central",
        "abertura_dia": 3,
        "status": "em analise",
        "conclusao_dia": None
    },
    {
        "id": "OC003",
        "categoria": "acessibilidade",
        "descricao": "Rampa de acesso danificada",
        "localidade": "Avenida Norte",
        "abertura_dia": 1,
        "status": "concluida",
        "conclusao_dia": 6
    },
    {
        "id": "OC004",
        "categoria": "conservacao",
        "descricao": "Banco da praca quebrado",
        "localidade": "Praca Sul",
        "abertura_dia": 4,
        "status": "aberta",
        "conclusao_dia": None
    },
    {
        "id": "OC005",
        "categoria": "iluminacao",
        "descricao": "Lampada com funcionamento intermitente",
        "localidade": "Rua Central",
        "abertura_dia": 5,
        "status": "em analise",
        "conclusao_dia": None
    },
    {
        "id": "OC006",
        "categoria": "limpeza",
        "descricao": "Descarte irregular de residuos",
        "localidade": "Rua do Lago",
        "abertura_dia": 2,
        "status": "concluida",
        "conclusao_dia": 7
    },
    {
        "id": "OC007",
        "categoria": "acessibilidade",
        "descricao": "Calcada com obstaculos",
        "localidade": "Avenida Sul",
        "abertura_dia": 6,
        "status": "aberta",
        "conclusao_dia": None
    },
    {
        "id": "OC008",
        "categoria": "conservacao",
        "descricao": "Playground necessita de manutencao",
        "localidade": "Parque Central",
        "abertura_dia": 3,
        "status": "em analise",
        "conclusao_dia": None
    },
    {
        "id": "OC009",
        "categoria": "iluminacao",
        "descricao": "Falta de iluminacao em travessa",
        "localidade": "Travessa Azul",
        "abertura_dia": 7,
        "status": "concluida",
        "conclusao_dia": 10
    },
    {
        "id": "OC010",
        "categoria": "limpeza",
        "descricao": "Lixeira publica danificada",
        "localidade": "Rua das Palmeiras",
        "abertura_dia": 8,
        "status": "aberta",
        "conclusao_dia": None
    },
    {
        "id": "OC011",
        "categoria": "acessibilidade",
        "descricao": "Piso irregular em calcada",
        "localidade": "Rua do Comercio",
        "abertura_dia": 5,
        "status": "em analise",
        "conclusao_dia": None
    },
    {
        "id": "OC012",
        "categoria": "conservacao",
        "descricao": "Vazamento em bebedouro publico",
        "localidade": "Praca Central",
        "abertura_dia": 9,
        "status": "concluida",
        "conclusao_dia": 12
    }
]

# Registro propositalmente inconsistente para testes de validacao
REGISTRO_INCONSISTENTE = {
    "id": "OC013",
    "categoria": "",
    "descricao": "Problema sem categoria informada",
    "localidade": "Rua das Flores",
    "abertura_dia": 10,
    "status": "aberta",
    "conclusao_dia": None
}

# Historico inicial com oito eventos simulados
HISTORICO_INICIAL = [
    {
        "id": "OC001",
        "dia": 2,
        "status_anterior": None,
        "status_novo": "aberta"
    },
    {
        "id": "OC002",
        "dia": 3,
        "status_anterior": None,
        "status_novo": "aberta"
    },
    {
        "id": "OC002",
        "dia": 4,
        "status_anterior": "aberta",
        "status_novo": "em analise"
    },
    {
        "id": "OC003",
        "dia": 1,
        "status_anterior": None,
        "status_novo": "aberta"
    },
    {
        "id": "OC003",
        "dia": 3,
        "status_anterior": "aberta",
        "status_novo": "em analise"
    },
    {
        "id": "OC003",
        "dia": 6,
        "status_anterior": "em analise",
        "status_novo": "concluida"
    },
    {
        "id": "OC006",
        "dia": 2,
        "status_anterior": None,
        "status_novo": "aberta"
    },
    {
        "id": "OC006",
        "dia": 7,
        "status_anterior": "em analise",
        "status_novo": "concluida"
    }
]

# ============================================
# FUNCOES DE CADASTRO E VALIDACAO
# ============================================


def validar_ocorrencia(ocorrencia, lista_ocorrencias):

    campos_obrigatorios = [
        "id",
        "categoria",
        "descricao",
        "localidade",
        "abertura_dia",
        "status"
    ]

    # Verifica campos obrigatorios
    for campo in campos_obrigatorios:

        if campo not in ocorrencia:
            return False, f"Campo ausente: {campo}"

        valor = ocorrencia[campo]

        if valor is None:
            return False, f"Campo vazio: {campo}"

        if isinstance(valor, str) and not valor.strip():
            return False, f"Campo vazio: {campo}"

    # Verifica identificador
    codigo = ocorrencia["id"]

    if not isinstance(codigo, str):
        return False, "Identificador deve ser texto"

    if not codigo.startswith("OC") or not codigo[2:].isdigit():
        return False, "Formato de identificador invalido!"

    for registro in lista_ocorrencias:

        if registro["id"] == codigo:
            return False, "Identificador ja cadastrado!"

    # Verifica categoria
    if ocorrencia["categoria"] not in CATEGORIAS:
        return False, "Categoria invalida!"

    # Verifica situacao
    if ocorrencia["status"] not in STATUS_VALIDOS:
        return False, "Situacao invalida!"

    # Verifica descricao e localidade
    # OR: rejeita quando o valor nao e texto OU esta vazio.
    if (
        not isinstance(ocorrencia["descricao"], str)
        or not ocorrencia["descricao"].strip()
    ):
        return False, "Descricao invalida!"

    if (
        not isinstance(ocorrencia["localidade"], str)
        or not ocorrencia["localidade"].strip()
    ):
        return False, "Localidade invalida!"

    # Verifica data simulada
    if type(ocorrencia["abertura_dia"]) != int:
        return False, "Dia de abertura deve ser inteiro!"

    if ocorrencia["abertura_dia"] < 1:
        return False, "Dia de abertura invalido!"

    # Verifica data de conclusao
    conclusao = ocorrencia.get("conclusao_dia")

    if ocorrencia["status"] == "concluida":

        if type(conclusao) != int:
            return False, "Ocorrencia concluida precisa de data de conclusao!"

        if conclusao < ocorrencia["abertura_dia"]:
            return False, "Data de conclusao anterior a abertura!"

    elif conclusao is not None:
        return False, "Ocorrencia nao concluida nao pode ter data de conclusao!"

    return True, "Ocorrencia valida!"



def cadastrar_ocorrencia(ocorrencia, estruturas):

    lista = estruturas["lista"]

    valido, mensagem = validar_ocorrencia(
        ocorrencia,
        lista
    )

    if not valido:
        return False, mensagem

    lista.append(ocorrencia)

    estruturas["dicionario"][ocorrencia["id"]] = ocorrencia

    categoria = ocorrencia["categoria"]

    estruturas["hierarquia"][BAIRRO][categoria].append(
        ocorrencia
    )

    # Atualiza a matriz de indicadores
    indice_categoria = CATEGORIAS.index(categoria)
    indice_status = STATUS_VALIDOS.index(ocorrencia["status"])

    estruturas["matriz"][indice_categoria][indice_status] += 1

    # Demandas abertas entram na fila
    if ocorrencia["status"] == "aberta":
        estruturas["fila"].append(ocorrencia["id"])


    evento = {
        "id": ocorrencia["id"],
        "dia": ocorrencia["abertura_dia"],
        "status_anterior": None,
        "status_novo": ocorrencia["status"]
    }

    estruturas["pilha"].append(evento)

    return True, "Ocorrencia cadastrada com sucesso!"

# ============================================
# ATUALIZACAO DE STATUS E HISTORICO
# ============================================

def atualizar_status(codigo, novo_status, dia, estruturas):

    ocorrencia = estruturas["dicionario"].get(codigo)

    if ocorrencia is None:
        return False, "Ocorrencia nao encontrada!"

    if novo_status not in STATUS_VALIDOS:
        return False, "Situacao desconhecida!"

    if novo_status == ocorrencia["status"]:
        return False, "A ocorrencia ja possui essa situacao!"

    if type(dia) != int or dia < ocorrencia["abertura_dia"]:
        return False, "Data simulada invalida!"

    status_anterior = ocorrencia["status"]
    categoria = ocorrencia["categoria"]

    # Atualiza a matriz
    indice_categoria = CATEGORIAS.index(categoria)
    indice_anterior = STATUS_VALIDOS.index(status_anterior)
    indice_novo = STATUS_VALIDOS.index(novo_status)

    estruturas["matriz"][indice_categoria][indice_anterior] -= 1
    estruturas["matriz"][indice_categoria][indice_novo] += 1

    # Atualiza a fila de atendimento
    fila = estruturas["fila"]

    if status_anterior == "aberta" and codigo in fila:
        fila.remove(codigo)

    elif novo_status == "aberta" and codigo not in fila:
        fila.append(codigo)

    # Registra o evento na pilha de historico
    evento = {
        "id": codigo,
        "dia": dia,
        "status_anterior": status_anterior,
        "status_novo": novo_status
    }

    estruturas["pilha"].append(evento)

    # Atualiza o registro principal
    ocorrencia["status"] = novo_status

    if novo_status == "concluida":
        ocorrencia["conclusao_dia"] = dia
    else:
        ocorrencia["conclusao_dia"] = None

    return True, "Situacao atualizada com sucesso!"

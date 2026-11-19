
# ============================================
# NEIGHBORHOOD ACTION DASHBOARD
# TESTES AUTOMATIZADOS
# ============================================

from copy import deepcopy

from ocorrencias import (
    OCORRENCIAS_INICIAIS,
    HISTORICO_INICIAL,
    REGISTRO_INCONSISTENTE,
    cadastrar_ocorrencia,
    atualizar_status
)

from estruturas import construir_estruturas


def verificar_consistencia(estruturas):

    lista = estruturas["lista"]
    dicionario = estruturas["dicionario"]
    fila = estruturas["fila"]
    hierarquia = estruturas["hierarquia"]
    matriz = estruturas["matriz"]

    # Verifica lista e dicionario
    assert len(lista) == len(dicionario)

    for ocorrencia in lista:
        codigo = ocorrencia["id"]

        assert codigo in dicionario
        assert dicionario[codigo] is ocorrencia

    # Verifica fila
    abertas = [
        ocorrencia["id"]
        for ocorrencia in lista
        if ocorrencia["status"] == "aberta"
    ]

    assert sorted(fila) == sorted(abertas)

    # Verifica hierarquia
    registros_hierarquia = []

    for categoria in hierarquia["Jardim Esperança"]:

        for ocorrencia in hierarquia["Jardim Esperança"][categoria]:
            registros_hierarquia.append(ocorrencia)

    assert len(registros_hierarquia) == len(lista)

    # Verifica matriz
    from ocorrencias import CATEGORIAS, STATUS_VALIDOS

    matriz_esperada = []

    for categoria in CATEGORIAS:

        linha = []

        for status in STATUS_VALIDOS:

            quantidade = 0

            for ocorrencia in lista:

                if (
                    ocorrencia["categoria"] == categoria
                    and ocorrencia["status"] == status
                ):
                    quantidade += 1

            linha.append(quantidade)

        matriz_esperada.append(linha)

    assert matriz == matriz_esperada

    return True


def executar_testes():

    print("\n======================================")
    print("   TESTES DO NEIGHBORHOOD DASHBOARD")
    print("======================================")

    estruturas = construir_estruturas(
        deepcopy(OCORRENCIAS_INICIAIS),
        deepcopy(HISTORICO_INICIAL)
    )

    # TESTE 1: dados iniciais
    assert len(estruturas["lista"]) == 12
    print("[OK] Inicializacao dos registros")

    # TESTE 2: registro inconsistente
    sucesso, mensagem = cadastrar_ocorrencia(
        deepcopy(REGISTRO_INCONSISTENTE),
        estruturas
    )

    assert sucesso is False
    assert len(estruturas["lista"]) == 12
    print("[OK] Bloqueio de registro inconsistente")

    # TESTE 3: cadastro valido
    nova = {
        "id": "OC013",
        "categoria": "limpeza",
        "descricao": "Lixeira cheia",
        "localidade": "Rua das Acacias",
        "abertura_dia": 13,
        "status": "aberta",
        "conclusao_dia": None
    }

    sucesso, mensagem = cadastrar_ocorrencia(
        nova,
        estruturas
    )

    assert sucesso is True
    assert "OC013" in estruturas["dicionario"]
    print("[OK] Cadastro de nova ocorrencia")

    # TESTE 4: identificador duplicado
    sucesso, mensagem = cadastrar_ocorrencia(
        nova.copy(),
        estruturas
    )

    assert sucesso is False
    print("[OK] Bloqueio de identificador duplicado")

    # TESTE 5: busca pelo identificador
    assert estruturas["dicionario"]["OC001"]["id"] == "OC001"
    print("[OK] Consulta por identificador")

    # TESTE 6: atualizacao valida
    sucesso, mensagem = atualizar_status(
        "OC001",
        "em analise",
        11,
        estruturas
    )

    assert sucesso is True
    assert estruturas["dicionario"]["OC001"]["status"] == "em analise"
    print("[OK] Atualizacao de situacao")

    # TESTE 7: atualizacao com status inexistente
    sucesso, mensagem = atualizar_status(
        "OC001",
        "cancelada",
        12,
        estruturas
    )

    assert sucesso is False
    print("[OK] Bloqueio de situacao desconhecida")

    # TESTE 8: atualizacao de registro inexistente
    sucesso, mensagem = atualizar_status(
        "OC999",
        "concluida",
        12,
        estruturas
    )

    assert sucesso is False
    print("[OK] Tratamento de registro inexistente")

    # TESTE 9: atualizacao com dia anterior a abertura
    sucesso, mensagem = atualizar_status(
        "OC001",
        "concluida",
        1,
        estruturas
    )

    assert sucesso is False
    print("[OK] Bloqueio de data invalida")

    # TESTE 10: conclusao
    sucesso, mensagem = atualizar_status(
        "OC001",
        "concluida",
        12,
        estruturas
    )

    assert sucesso is True
    assert estruturas["dicionario"]["OC001"]["conclusao_dia"] == 12
    print("[OK] Conclusao de ocorrencia")

    # TESTE 11: reabertura
    sucesso, mensagem = atualizar_status(
        "OC001",
        "aberta",
        13,
        estruturas
    )

    assert sucesso is True
    assert "OC001" in estruturas["fila"]
    assert estruturas["dicionario"]["OC001"]["conclusao_dia"] is None
    print("[OK] Reabertura e retorno para fila")

    # TESTE 12: historico
    assert len(estruturas["pilha"]) == 12
    print("[OK] Registro de eventos no historico")

    # TESTE 13: consistencia entre estruturas
    assert verificar_consistencia(estruturas)
    print("[OK] Consistencia entre estruturas de dados")

    print("\n======================================")
    print("TODOS OS 13 TESTES PASSARAM!")
    print("======================================")


if __name__ == "__main__":
    executar_testes()


# ============================================
# ESTRUTURAS DE DADOS
# ============================================

from ocorrencias import (
    BAIRRO,
    CATEGORIAS,
    STATUS_VALIDOS,
    OCORRENCIAS_INICIAIS,
    HISTORICO_INICIAL
)


def construir_estruturas(ocorrencias, historico):

    # 1. LISTA: conjunto completo de ocorrencias
    lista_ocorrencias = ocorrencias.copy()

    # 2. FILA: ocorrencias abertas aguardando analise
    fila_atendimento = []

    for ocorrencia in lista_ocorrencias:
        if ocorrencia["status"] == "aberta":
            fila_atendimento.append(ocorrencia["id"])

    # 3. PILHA: eventos de historico
    pilha_historico = historico.copy()

    # 4. DICIONARIO: acesso rapido pelo identificador
    ocorrencias_por_id = {}

    for ocorrencia in lista_ocorrencias:
        ocorrencias_por_id[ocorrencia["id"]] = ocorrencia

    # 5. HIERARQUIA: bairro -> categoria -> ocorrencias
    hierarquia = {
        BAIRRO: {}
    }

    for categoria in CATEGORIAS:
        hierarquia[BAIRRO][categoria] = []

    for ocorrencia in lista_ocorrencias:
        categoria = ocorrencia["categoria"]

        hierarquia[BAIRRO][categoria].append(
            ocorrencia
        )

    # 6. MATRIZ: categorias x situacoes
    matriz_indicadores = []

    for categoria in CATEGORIAS:
        linha = []

        for status in STATUS_VALIDOS:
            quantidade = 0

            for ocorrencia in lista_ocorrencias:
                if (
                    ocorrencia["categoria"] == categoria
                    and ocorrencia["status"] == status
                ):
                    quantidade += 1

            linha.append(quantidade)

        matriz_indicadores.append(linha)

    return {
        "lista": lista_ocorrencias,
        "fila": fila_atendimento,
        "pilha": pilha_historico,
        "dicionario": ocorrencias_por_id,
        "hierarquia": hierarquia,
        "matriz": matriz_indicadores
    }


# Teste inicial das estruturas
if __name__ == "__main__":

    estruturas = construir_estruturas(
        OCORRENCIAS_INICIAIS,
        HISTORICO_INICIAL
    )

    print("ESTRUTURAS INICIALIZADAS")
    print("--------------------------------")

    print("Ocorrencias:", len(estruturas["lista"]))
    print("Fila de atendimento:", len(estruturas["fila"]))
    print("Eventos no historico:", len(estruturas["pilha"]))
    print("Registros no dicionario:", len(estruturas["dicionario"]))

    print("\nMATRIZ DE INDICADORES")
    print("Categoria | Aberta | Em analise | Concluida")

    for indice, categoria in enumerate(CATEGORIAS):
        print(categoria, estruturas["matriz"][indice])

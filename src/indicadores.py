
# ============================================
# NEIGHBORHOOD ACTION DASHBOARD
# MODULO DE INDICADORES
# ============================================

from ocorrencias import CATEGORIAS, STATUS_VALIDOS


def calcular_indicadores(estruturas):

    lista = estruturas["lista"]

    total = len(lista)

    # Contadores por situacao
    quantidade_status = {
        status: 0 for status in STATUS_VALIDOS
    }

    # Contadores por categoria
    quantidade_categoria = {
        categoria: 0 for categoria in CATEGORIAS
    }

    # Acumuladores para o tempo medio
    soma_tempo_conclusao = 0
    total_concluidas_com_tempo = 0

    # Percorre todas as ocorrencias
    for ocorrencia in lista:

        categoria = ocorrencia["categoria"]
        status = ocorrencia["status"]

        quantidade_categoria[categoria] += 1
        quantidade_status[status] += 1

        # Calcula tempo apenas das ocorrencias concluidas
        if (
            status == "concluida"
            and ocorrencia["conclusao_dia"] is not None
        ):

            tempo = (
                ocorrencia["conclusao_dia"]
                - ocorrencia["abertura_dia"]
            )

            if tempo >= 0:
                soma_tempo_conclusao += tempo
                total_concluidas_com_tempo += 1

    # Calcula os percentuais por situacao
    percentuais_status = {}

    for status in STATUS_VALIDOS:

        if total > 0:
            percentual = (
                quantidade_status[status] / total
            ) * 100
        else:
            percentual = 0

        percentuais_status[status] = percentual

    # Calcula os percentuais por categoria
    percentuais_categoria = {}

    for categoria in CATEGORIAS:

        if total > 0:
            percentual = (
                quantidade_categoria[categoria] / total
            ) * 100
        else:
            percentual = 0

        percentuais_categoria[categoria] = percentual

    # Total de demandas pendentes
    pendentes = (
        quantidade_status["aberta"]
        + quantidade_status["em analise"]
    )

    # Percentual de conclusao
    if total > 0:
        percentual_conclusao = (
            quantidade_status["concluida"] / total
        ) * 100
    else:
        percentual_conclusao = 0

    # Tempo medio de conclusao
    if total_concluidas_com_tempo > 0:

        tempo_medio = (
            soma_tempo_conclusao
            / total_concluidas_com_tempo
        )

    else:
        tempo_medio = 0

    return {
        "total": total,
        "quantidade_status": quantidade_status,
        "quantidade_categoria": quantidade_categoria,
        "percentuais_status": percentuais_status,
        "percentuais_categoria": percentuais_categoria,
        "pendentes": pendentes,
        "percentual_conclusao": percentual_conclusao,
        "tempo_medio": tempo_medio,
        "total_concluidas_com_tempo": total_concluidas_com_tempo
    }


def exibir_indicadores(estruturas):

    dados = calcular_indicadores(estruturas)

    print("\n" + "=" * 55)
    print("          PAINEL DE INDICADORES")
    print("=" * 55)

    print("\nRESUMO GERAL")

    print("Total de ocorrencias:", dados["total"])

    print("Demandas pendentes:", dados["pendentes"])

    print(
        "Percentual de conclusao:",
        f'{dados["percentual_conclusao"]:.2f}%'
    )

    print("\nDISTRIBUICAO POR SITUACAO")

    for status in STATUS_VALIDOS:

        quantidade = dados["quantidade_status"][status]
        percentual = dados["percentuais_status"][status]

        print(
            f"{status}: {quantidade} ocorrencias "
            f"({percentual:.2f}%)"
        )

    print("\nDISTRIBUICAO POR CATEGORIA")

    for categoria in CATEGORIAS:

        quantidade = dados["quantidade_categoria"][categoria]
        percentual = dados["percentuais_categoria"][categoria]

        print(
            f"{categoria}: {quantidade} ocorrencias "
            f"({percentual:.2f}%)"
        )

    print("\nTEMPO MEDIO DE CONCLUSAO")

    if dados["total_concluidas_com_tempo"] > 0:

        print(
            f'{dados["tempo_medio"]:.2f} dias simulados'
        )

    else:
        print("Ainda nao existem conclusoes com tempo valido.")

    print("\n" + "=" * 55)

    interpretar_indicadores(dados)



def interpretar_indicadores(dados):

    print("\nINTERPRETACAO DOS RESULTADOS")
    print("-" * 55)

    if dados["total"] == 0:
        print("Nao existem ocorrencias para analisar.")
        return

    # Identifica a maior quantidade por categoria
    maior_quantidade = max(
        dados["quantidade_categoria"].values()
    )

    categorias_prioritarias = [
        categoria
        for categoria, quantidade
        in dados["quantidade_categoria"].items()
        if quantidade == maior_quantidade
    ]

    if len(categorias_prioritarias) > 1:
        print(
            "Categorias com maior quantidade: "
            + ", ".join(categorias_prioritarias)
            + f", com {maior_quantidade} ocorrencias cada."
        )
    else:
        print(
            f"A categoria com maior quantidade e "
            f"{categorias_prioritarias[0]}, "
            f"com {maior_quantidade} ocorrencias."
        )

    # Analisa as demandas pendentes
    percentual_pendente = (
        dados["pendentes"] / dados["total"]
    ) * 100

    if percentual_pendente > 50:
        print("Mais da metade das demandas permanece pendente.")

    elif percentual_pendente == 50:
        print("Metade das demandas permanece pendente.")

    else:
        print("Menos da metade das demandas permanece pendente.")

    # Analisa a conclusao
    if dados["percentual_conclusao"] > 50:
        print("A maioria das ocorrencias foi concluida.")

    elif dados["percentual_conclusao"] == 50:
        print("Metade das ocorrencias foi concluida.")

    else:
        print("Menos da metade das ocorrencias foi concluida.")

    print(
        "\nOs resultados representam exclusivamente dados simulados "
        "e nao indicam o desempenho de orgaos publicos reais."
    )


    # Identifica a categoria com maior quantidade
    categoria_prioritaria = max(
        dados["quantidade_categoria"],
        key=dados["quantidade_categoria"].get
    )

    quantidade = dados["quantidade_categoria"][
        categoria_prioritaria
    ]

    print(
        f"A categoria com maior quantidade de registros e "
        f"{categoria_prioritaria}, com {quantidade} ocorrencias."
    )

    # Analisa as demandas pendentes
    percentual_pendente = (
        dados["pendentes"] / dados["total"]
    ) * 100

    if percentual_pendente >= 50:

        print(
            "Mais da metade das demandas permanece pendente. "
            "O conjunto simulado indica necessidade de maior acompanhamento."
        )

    else:

        print(
            "Menos da metade das demandas permanece pendente. "
            "O conjunto simulado apresenta uma quantidade menor de pendencias."
        )

    # Analisa a conclusao
    if dados["percentual_conclusao"] >= 50:

        print(
            "A maioria das ocorrencias foi concluida."
        )

    else:

        print(
            "A maioria das ocorrencias ainda nao foi concluida."
        )

    print(
        "\nOs resultados representam exclusivamente dados simulados "
        "e nao indicam o desempenho de orgaos publicos reais."
    )

def exibir_matriz(estruturas):

    print("\n" + "=" * 65)
    print("          MATRIZ DE OCORRENCIAS")
    print("=" * 65)

    print(
        f"{'CATEGORIA':<20}"
        f"{'ABERTA':<12}"
        f"{'EM ANALISE':<16}"
        f"{'CONCLUIDA':<12}"
    )

    matriz = estruturas["matriz"]

    for indice, categoria in enumerate(CATEGORIAS):

        linha = matriz[indice]

        print(
            f"{categoria:<20}"
            f"{linha[0]:<12}"
            f"{linha[1]:<16}"
            f"{linha[2]:<12}"
        )

    print("=" * 65)

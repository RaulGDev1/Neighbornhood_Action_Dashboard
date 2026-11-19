
# ============================================
# NEIGHBORHOOD ACTION DASHBOARD
# Sistema principal
# ============================================

from indicadores import exibir_indicadores, exibir_matriz

from ocorrencias import (
    BAIRRO,
    CATEGORIAS,
    STATUS_VALIDOS,
    OCORRENCIAS_INICIAIS,
    HISTORICO_INICIAL,
    REGISTRO_INCONSISTENTE,
    cadastrar_ocorrencia,
    atualizar_status
)

from estruturas import construir_estruturas


def ler_inteiro(mensagem):

    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um numero inteiro valido!")


def exibir_ocorrencia(ocorrencia):

    print("-" * 55)
    print("Codigo:", ocorrencia["id"])
    print("Categoria:", ocorrencia["categoria"])
    print("Descricao:", ocorrencia["descricao"])
    print("Local:", ocorrencia["localidade"])
    print("Abertura: Dia", ocorrencia["abertura_dia"])
    print("Situacao:", ocorrencia["status"])

    if ocorrencia["conclusao_dia"] is not None:
        print("Conclusao: Dia", ocorrencia["conclusao_dia"])

    print("-" * 55)


def listar_ocorrencias(estruturas):

    print("\n========== TODAS AS OCORRENCIAS ==========")

    lista = estruturas["lista"]

    if not lista:
        print("Nenhuma ocorrencia cadastrada.")
        return

    for ocorrencia in lista:
        exibir_ocorrencia(ocorrencia)


def consultar_por_codigo(estruturas):

    codigo = input("\nDigite o codigo da ocorrencia: ").strip().upper()

    ocorrencia = estruturas["dicionario"].get(codigo)

    if ocorrencia is None:
        print("Ocorrencia nao encontrada!")
    else:
        exibir_ocorrencia(ocorrencia)


def filtrar_ocorrencias(estruturas, campo, valor):

    resultados = []

    for ocorrencia in estruturas["lista"]:

        if ocorrencia[campo] == valor:
            resultados.append(ocorrencia)

    if not resultados:
        print("\nNenhuma ocorrencia encontrada com esse filtro.")
        return

    print("\n========== RESULTADOS ==========")

    for ocorrencia in resultados:
        exibir_ocorrencia(ocorrencia)


def filtrar_por_categoria(estruturas):

    print("\nCategorias disponiveis:")

    for categoria in CATEGORIAS:
        print("-", categoria)

    categoria = input("\nDigite a categoria: ").strip().lower()

    if categoria not in CATEGORIAS:
        print("Categoria invalida!")
        return

    filtrar_ocorrencias(
        estruturas,
        "categoria",
        categoria
    )


def filtrar_por_status(estruturas):

    print("\nSituacoes disponiveis:")

    for status in STATUS_VALIDOS:
        print("-", status)

    status = input("\nDigite a situacao: ").strip().lower()

    if status not in STATUS_VALIDOS:
        print("Situacao invalida!")
        return

    filtrar_ocorrencias(
        estruturas,
        "status",
        status
    )


def gerar_codigo(estruturas):

    maior_codigo = 0

    for ocorrencia in estruturas["lista"]:
        numero = int(ocorrencia["id"][2:])

        if numero > maior_codigo:
            maior_codigo = numero

    return f"OC{maior_codigo + 1:03d}"


def cadastrar_nova_ocorrencia(estruturas):

    print("\n========== NOVA OCORRENCIA ==========")

    print("\nCategorias disponiveis:")

    for categoria in CATEGORIAS:
        print("-", categoria)

    categoria = input("\nCategoria: ").strip().lower()

    if categoria not in CATEGORIAS:
        print("Categoria invalida!")
        return

    descricao = input("Descricao: ").strip()
    localidade = input("Localidade generica: ").strip()
    abertura_dia = ler_inteiro("Dia simulado de abertura: ")

    codigo = gerar_codigo(estruturas)

    nova_ocorrencia = {
        "id": codigo,
        "categoria": categoria,
        "descricao": descricao,
        "localidade": localidade,
        "abertura_dia": abertura_dia,
        "status": "aberta",
        "conclusao_dia": None
    }

    sucesso, mensagem = cadastrar_ocorrencia(
        nova_ocorrencia,
        estruturas
    )

    print("\n", mensagem)

    if sucesso:
        print("Codigo gerado:", codigo)


def alterar_situacao(estruturas):

    print("\n========== ATUALIZAR SITUACAO ==========")

    codigo = input("Codigo da ocorrencia: ").strip().upper()

    ocorrencia = estruturas["dicionario"].get(codigo)

    if ocorrencia is None:
        print("Ocorrencia nao encontrada!")
        return

    print("\nSituacao atual:", ocorrencia["status"])

    print("\nSituacoes disponiveis:")

    for status in STATUS_VALIDOS:
        print("-", status)

    novo_status = input("\nNova situacao: ").strip().lower()

    dia = ler_inteiro("Dia simulado da atualizacao: ")

    sucesso, mensagem = atualizar_status(
        codigo,
        novo_status,
        dia,
        estruturas
    )

    print("\n", mensagem)


def consultar_historico(estruturas):

    print("\n========== HISTORICO DE ATUALIZACOES ==========")

    codigo = input("Codigo da ocorrencia: ").strip().upper()

    if codigo not in estruturas["dicionario"]:
        print("Ocorrencia nao encontrada!")
        return

    eventos = []

    for evento in estruturas["pilha"]:
        if evento["id"] == codigo:
            eventos.append(evento)

    if not eventos:
        print("Nenhum evento encontrado.")
        return

    print("\nEventos mais recentes primeiro:")

    for evento in reversed(eventos):
        print(
            "Dia", evento["dia"],
            "|", evento["status_anterior"],
            "->", evento["status_novo"]
        )


def consultar_fila(estruturas):

    print("\n========== FILA DE ATENDIMENTO ==========")

    fila = estruturas["fila"]

    if not fila:
        print("Nao existem demandas aguardando analise.")
        return

    for posicao, codigo in enumerate(fila, start=1):
        print(posicao, "-", codigo)


def menu_principal():

    print("\n" + "=" * 55)
    print("       NEIGHBORHOOD ACTION DASHBOARD")
    print("=" * 55)
    print("Bairro:", BAIRRO)
    print("-" * 55)

    print("[1] Cadastrar ocorrencia")
    print("[2] Listar ocorrencias")
    print("[3] Consultar por identificador")
    print("[4] Filtrar por categoria")
    print("[5] Filtrar por situacao")
    print("[6] Atualizar situacao")
    print("[7] Consultar historico")
    print("[8] Consultar fila de atendimento")
    print("[9] Painel de indicadores")
    print("[10] Matriz de ocorrencias")
    print("[0] Encerrar sistema")

    print("=" * 55)


def iniciar_sistema():

    estruturas = construir_estruturas(
        OCORRENCIAS_INICIAIS,
        HISTORICO_INICIAL
    )

    print("\nSistema inicializado com sucesso!")

    # Testa a validacao do registro inconsistente
    print("\nVerificando registro de teste...")

    valido, mensagem = cadastrar_ocorrencia(
        REGISTRO_INCONSISTENTE.copy(),
        estruturas
    )

    print(mensagem)

    while True:

        menu_principal()

        opcao = input("Selecione uma opcao: ").strip()

        if opcao == "1":
            cadastrar_nova_ocorrencia(estruturas)

        elif opcao == "2":
            listar_ocorrencias(estruturas)

        elif opcao == "3":
            consultar_por_codigo(estruturas)

        elif opcao == "4":
            filtrar_por_categoria(estruturas)

        elif opcao == "5":
            filtrar_por_status(estruturas)

        elif opcao == "6":
            alterar_situacao(estruturas)

        elif opcao == "7":
            consultar_historico(estruturas)

        elif opcao == "8":
            consultar_fila(estruturas)

        elif opcao == "9":
            exibir_indicadores(estruturas)

        elif opcao =="10":
            exibir_matriz(estruturas)

        elif opcao == "0":
            print("\nEncerrando o sistema...")
            print("Obrigado por utilizar o Neighborhood Action Dashboard!")
            break

        else:
            print("\nOpcao invalida! Tente novamente.")


if __name__ == "__main__":
    iniciar_sistema()

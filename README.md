Neighborhood Action Dashboard
1. Identificação
- Projeto: Neighborhood Action Dashboard
- Desafio: Global Solution – 2º Semestre de 2026
- Tema: CitizenTech
- Integrante: Raul Giampaulo Peres
- RM: 575720
- Curso: Ciência da Computação – FIAP
- Modalidade: Desenvolvimento individual
2. Sobre o projeto
O Neighborhood Action Dashboard é um sistema desenvolvido em Python para simular o cadastro, a organização e o acompanhamento de ocorrências comunitárias.

O projeto foi desenvolvido com base no desafio CitizenTech, que propõe a utilização da tecnologia para auxiliar na identificação e organização de problemas cotidianos presentes nos bairros e comunidades.

A comunidade utilizada na simulação é o bairro fictício Jardim Esperança.

O sistema trabalha com quatro categorias de ocorrências:
- Iluminação;
- Acessibilidade;
- Limpeza;
- Conservação de espaços coletivos.
O público beneficiado pela proposta são moradores e pessoas interessadas na organização e no acompanhamento de demandas comunitárias.

Os registros são fictícios e não representam solicitações reais encaminhadas a órgãos públicos.
3. Funcionalidades
O sistema disponibiliza as seguintes funcionalidades:
- Cadastro de novas ocorrências;
- Listagem de ocorrências cadastradas;
- Consulta por identificador;
- Filtro por categoria;
- Filtro por situação;
- Atualização de situação;
- Consulta ao histórico de alterações;
- Consulta à fila de ocorrências abertas;
- Painel de indicadores;
- Matriz de ocorrências por categoria e situação.
Situações disponíveis
Situação	Significado
Aberta	Ocorrência registrada e aguardando análise.
Em análise	Ocorrência em acompanhamento simulado.
Concluída	Ocorrência finalizada na simulação.


4. Estruturas de dados utilizadas
O projeto utiliza diferentes estruturas de dados estudadas nas fases iniciais do curso.
Lista
Armazena o conjunto completo de ocorrências, permitindo percorrer os registros e realizar consultas.
Fila
Organiza as ocorrências abertas que aguardam análise, respeitando a ordem de entrada.
Pilha
Armazena os eventos de acompanhamento e as alterações de situação. Os eventos mais recentes podem ser consultados primeiro.
Dicionário
Permite localizar uma ocorrência diretamente pelo identificador, facilitando as consultas e o acesso aos registros.
Estrutura hierárquica
Organiza os dados seguindo a estrutura:

Bairro → Categoria → Ocorrências

Essa organização facilita a separação e a consulta das demandas de acordo com sua categoria.
Matriz
Utiliza uma lista de listas para representar a quantidade de ocorrências por categoria e situação.

As linhas representam as categorias e as colunas representam as situações. Essa estrutura permite visualizar a distribuição dos registros de forma organizada.
5. Regras lógicas e validações
O sistema utiliza estruturas condicionais (if, elif e else) e operadores booleanos para controlar as operações.

Entre as validações implementadas estão:
- Impedir cadastro sem campos obrigatórios;
- Bloquear identificadores duplicados;
- Verificar categorias permitidas;
- Impedir situações desconhecidas;
- Validar datas simuladas;
- Impedir atualizações de ocorrências inexistentes;
- Rejeitar descrições e localidades inválidas;
- Impedir atualizações para a mesma situação, quando essa regra é aplicada pela função de atualização.
Operadores booleanos
AND: utilizado na verificação da matriz para identificar ocorrências que pertencem simultaneamente a uma categoria e a uma situação.

Exemplo:
if (
    ocorrencia["categoria"] == categoria
    and ocorrencia["status"] == status
):
    quantidade += 1
OR: utilizado para rejeitar uma descrição quando ela não é texto ou quando está vazia.

Exemplo:
if (
    not isinstance(ocorrencia["descricao"], str)
    or not ocorrencia["descricao"].strip()
):
    return False, "Descricao invalida!"
NOT: utilizado para verificar uma condição negativa, como a ausência de conteúdo em um campo obrigatório.

Exemplo:
if not ocorrencia["descricao"].strip():
    return False, "Descricao invalida!"
As condições permitem validar entradas, filtrar registros e evitar operações com dados inconsistentes.
6. Indicadores implementados
O sistema calcula indicadores utilizando laços, operações matemáticas e estruturas de dados.
Indicadores disponíveis
- Total de ocorrências;
- Quantidade por categoria;
- Quantidade por situação;
- Percentual por categoria;
- Percentual por situação;
- Quantidade de demandas pendentes;
- Percentual de conclusão;
- Tempo médio simulado de conclusão.
Fórmulas utilizadas
Percentual por categoria:

Quantidade da categoria / Total de ocorrências × 100.

Percentual por situação:

Quantidade da situação / Total de ocorrências × 100.

Demandas pendentes:

Ocorrências abertas + ocorrências em análise.

Percentual de conclusão:

Ocorrências concluídas / Total de ocorrências × 100.

Tempo médio de conclusão:

Soma dos tempos de conclusão válidos / Quantidade de ocorrências concluídas com tempo válido.
Interpretação
Os indicadores permitem identificar quais categorias apresentam maior quantidade de registros e quantas demandas permanecem pendentes.

Os resultados ajudam a compreender a distribuição das necessidades na comunidade simulada, sem representar dados reais de atendimento público.
7. Dados simulados
O sistema inicializa 12 ocorrências válidas diretamente no código Python, sem depender de arquivos CSV ou TXT externos.

Os registros estão distribuídos entre as quatro categorias:
- Iluminação;
- Acessibilidade;
- Limpeza;
- Conservação de espaços coletivos.
São utilizadas três situações distintas:
- Aberta;
- Em análise;
- Concluída.
O histórico inicial contém oito eventos simulados de acompanhamento.

Também existe um registro propositalmente inconsistente, sem categoria, utilizado para demonstrar o funcionamento das validações.
8. Organização dos arquivos
A estrutura do projeto está organizada da seguinte forma:
Neighborhood-Action-Dashboard/
│
├── README.md
├── .gitignore
│
├── src/
│   ├── sistema.py
│   ├── ocorrencias.py
│   ├── estruturas.py
│   ├── indicadores.py
│   └── testes.py
│
└── docs/
    ├── relatorio.pdf
    ├── link_video.txt
    └── uso_ia.md
Os dados são inicializados nos módulos Python, conforme explicado na seção anterior. Por isso, não existe um arquivo externo data/dados.csv.
9. Como executar
Requisitos
- Python 3 instalado;
- Visual Studio Code ou terminal compatível.
Executar o sistema
Na pasta principal do projeto, execute:
python src/sistema.py
Executar os testes automatizados
Para verificar as funcionalidades e a consistência das estruturas de dados, execute:
python src/testes.py
A suíte de testes foi executada com sucesso, com 13 testes aprovados na versão testada do projeto.
10. Exemplo de funcionamento
Cadastro
Uma nova ocorrência pode ser cadastrada informando:
- Categoria;
- Descrição;
- Localidade genérica;
- Dia simulado de abertura.
O sistema gera automaticamente um identificador único, conforme a implementação do cadastro.
Consulta
O usuário pode pesquisar uma ocorrência utilizando seu identificador e realizar filtros por categoria ou situação.
Atualização
Uma ocorrência existente pode ter sua situação alterada entre os estados permitidos.

Cada alteração válida é registrada no histórico.
Indicadores
Após as operações, o painel apresenta os totais e percentuais atualizados de acordo com os registros existentes.
11. Acessibilidade, inclusão e privacidade
O projeto considera os seguintes cuidados:
- Utilização de interface textual simples;
- Mensagens objetivas e compreensíveis;
- Informações organizadas por categorias e situações;
- Utilização de localidades genéricas;
- Ausência de dados pessoais de moradores;
- Utilização exclusiva de dados fictícios.
A proposta busca facilitar a compreensão das informações por diferentes usuários.
12. Utilização de inteligência artificial
A inteligência artificial foi utilizada como ferramenta de apoio durante o desenvolvimento do projeto.

Seu uso auxiliou na organização da estrutura do sistema, elaboração e revisão de funções, identificação de erros, preparação de testes e organização da documentação.

As sugestões foram avaliadas e revisadas durante o desenvolvimento. O código foi executado e testado no ambiente local, com acompanhamento do desenvolvedor.

A utilização da ferramenta não substituiu a necessidade de compreender, revisar e validar as implementações.
13. Limitações do projeto
O sistema possui caráter demonstrativo e utiliza dados simulados.

As informações são armazenadas em memória durante a execução, não possuindo persistência após o encerramento do programa.

Também não existe integração com prefeituras, órgãos públicos, serviços externos ou sistemas reais de atendimento.

As datas utilizadas são simuladas e não representam prazos reais.
14. Conclusão e aprendizados
O desenvolvimento do Neighborhood Action Dashboard permitiu aplicar conhecimentos de programação em Python, lógica booleana, estruturas de dados, algoritmos de busca, validação e análise de indicadores.

A utilização de listas, filas, pilhas, dicionários e matrizes demonstrou diferentes formas de organizar e consultar informações.

O projeto também permitiu compreender como uma aplicação simples pode transformar registros isolados em informações organizadas e indicadores compreensíveis.

Como aprendizado, destacou-se a importância da validação de dados, da consistência entre estruturas e da apresentação responsável dos resultados.
15. Apresentação
Vídeo de apresentação:
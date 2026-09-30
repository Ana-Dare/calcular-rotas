# 🗺️ Calculador de Rotas Terrestres entre Países (TDA Grafo)

Aplicação desenvolvida em Python. O sistema consome dados geográficos de países, constrói uma **Estrutura de Dados (TDA) Grafo** baseada em lista de adjacência e aplica o algoritmo de **Busca em Largura (BFS)** para calcular a menor rota terrestre (menor número de travessias de fronteira) entre dois países, renderizando o resultado em um mapa interativo.

Aplicação desenvolvida em Python. O sistema consome dados geográficos de países, para calcular a menor rota terrestre (menor número de travessias de fronteira) entre dois países, renderizando o resultado em um mapa interativo.

---

## 🚀 Funcionalidades

- **TDA Grafo Customizada:** Construção manual da estrutura de Grafo Não-Dirigido (com classes `GrafoPaises` e manipuladores de vértices/arestas) sem uso de bibliotecas externas de grafos.
- **Busca em Largura (BFS):** Algoritmo de busca determinística com complexidade de tempo $O(V + E)$ para encontrar o caminho com menor quantidade de fronteiras.
- **Visualização Geográfica:** Renderização gráfica da rota, marcadores e linhas de conexão em mapa interativo via Folium/Leaflet e MapTiler.
- **Arquitetura Modular (SOLID):** Separação de responsabilidades isolando o domínio da TDA (`domain/`), os serviços de dados e mapas (`services/`), as configurações (`config.py`) e os orquestradores de execução.
- **Interfaces de Uso:** Execução via Dashboard Web interativo com Streamlit.

---

## 📁 Estrutura do Projeto

```text
calcular-rotas/
├── config.py                # Configurações globais e chave de API do MapTiler
├── domain/
│   └── graph.py             # Implementação da TDA Grafo e Algoritmo BFS
├── services/
│   ├── country_service.py   # Consumo e conversão de dados da API para o Grafo
│   └── map_service.py       # Renderização gráfica do mapa via Folium
├── main.py                  # Ponto de entrada: Terminal Interativo + Abertura Automática
├── app.py                   # Ponto de entrada: Dashboard Web Interativo (Streamlit)
└── requirements.txt         # Arquivo de dependências do projeto
```

---

## ⚙️ Pré-requisitos

Antes de iniciar, certifique-se de ter instalado em sua máquina:

- **Python 3.10+**
- **pip** (Gerenciador de pacotes do Python)

---

## 📦 Passo a Passo de Instalação e Configuração

### 1. Clonar ou Baixar o Repositório

```bash
git clone [https://github.com/Ana-Dare/calcular-rotas]
cd trabalho-pa-3bi
```

### 2. Criar e Ativar um Ambiente Virtual (Recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate # Windows
```

### 3. Instalar as Dependências

requests
folium
streamlit
streamlit-folium

## 🛠️ Como Executar o Projeto

Você pode rodar a aplicação de duas formas:

### Execução via Dashboard Web (Streamlit)

Inicia uma aplicação web no seu navegador com caixas de seleção (_dropdowns_) de origem e destino, renderizando o mapa interativo diretamente na página.

```bash
streamlit run app.py
# ou iniciando o o arquivo main.py
```

## 📚 Arquitetura e Princípios SOLID

- **Single Responsibility Principle (SRP):** Cada arquivo/classe possui um único papel na aplicação.
  - `graph.py`: Cuida exclusivamente da estrutura de dados e busca algorítmica.
  - `country_service.py`: Cuida exclusivamente da comunicação HTTP e parsing do JSON.
  - `map_service.py`: Cuida exclusivamente do desenho dos componentes visuais no Folium.
- **Open/Closed Principle (OCP):** A TDA de Grafo pode receber novas implementações de busca (como Dijkstra ou A\*) sem alterar a camada visual ou de ingestão de dados.

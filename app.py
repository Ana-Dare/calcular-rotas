import streamlit as st
from config import MAPTILER_KEY
from services.country_service import CountryService
from services.map_service import MapService

st.set_page_config(page_title="Calculador de Rotas - TDA Grafo", layout="wide")

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 1rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }

        .stMainBlockContainer > div:first-child {
            margin-top: 0rem;
        }

        h1 {
            color: #FFF !important;
            font-size: 1.8rem !important;
            font-family: 'Segoe UI', Roboto, sans-serif !important;
            
        }

        div[data-testid="stButton"] button[data-testid="stBaseButton-primary"] {
            background-color: #000 !important;
            color: white !important;
            border-radius: 8px !important;
            border: solid 1px #F5F5F5 !important;
            font-weight: bold !important;
        }

        
    </style>
    """,
    unsafe_allow_html=True
)

@st.cache_data
def carregar_dados():
    service = CountryService()
    return service.carregar_dados_e_grafo()

st.title("Calculador de Rota Terrestre entre Países")

paises, grafo = carregar_dados()
map_service = MapService(api_key=MAPTILER_KEY)

mapeamento_paises = {f"{info['nome']} ({code})": code for code, info in paises.items()}
nomes_ordenados = sorted(list(mapeamento_paises.keys()))

col1, col2 = st.columns(2)
with col1:
    origem_padrao = [n for n in nomes_ordenados if "(BRA)" in n]
    idx_origem = nomes_ordenados.index(origem_padrao[0]) if origem_padrao else 0
    origem_selecionada = st.selectbox("Selecione o País de Origem:", nomes_ordenados, index=idx_origem)

with col2:
    destino_padrao = [n for n in nomes_ordenados if "(CAN)" in n]
    idx_destino = nomes_ordenados.index(destino_padrao[0]) if destino_padrao else 1
    destino_selecionado = st.selectbox("Selecione o País de Destino:", nomes_ordenados, index=idx_destino)

# Inicializa o estado do caminho na sessão do Streamlit
if "caminho" not in st.session_state:
    st.session_state.caminho = None
    st.session_state.calculado = False

# Cálculo executado ao clicar no botão
if st.button("Calcular e Visualizar Rota", type="primary"):
    code_origem = mapeamento_paises[origem_selecionada]
    code_destino = mapeamento_paises[destino_selecionado]

    with st.spinner("Calculando o menor caminho via BFS..."):
        st.session_state.caminho = grafo.buscar_menor_caminho_bfs(code_origem, code_destino)
        st.session_state.calculado = True

# Feedback de rota encontrada ou erro
if st.session_state.calculado:
    if st.session_state.caminho:
        st.success(f"Caminho encontrado em {len(st.session_state.caminho) - 1} travessias de fronteira!")
        nomes_rota = [paises[code]['nome'] for code in st.session_state.caminho if code in paises]
        st.write(" **Rota:** " + " ➔ ".join(nomes_rota))
    else:
        st.error("Não existe rota terrestre entre os países selecionados.")

map_service.gerar_mapa_rota(paises, st.session_state.caminho, output_filename="mapa_temp.html")
with open("mapa_temp.html", "r", encoding="utf-8") as f:
    st.components.v1.html(f.read(), height=600)
import requests
from config import COUNTRIES_API_URL
from domain.graph import GrafoPaises

class CountryService:
    """Serviço para busca de dados geográficos e montagem da TDA."""

    def __init__(self, api_url: str = COUNTRIES_API_URL):
        self.api_url = api_url

    def carregar_dados_e_grafo(self) -> tuple[dict, GrafoPaises]:
        response = requests.get(self.api_url)
        if response.status_code != 200:
            raise Exception(f"Erro ao acessar API (Status {response.status_code})")

        dados_api = response.json()
        grafo = GrafoPaises()
        paises_dict = {}

        # Popula os vértices do Grafo e salva dicionário de metadados
        for p in dados_api:
            code = p.get("cca3")
            if code:
                nome = p.get("name", {}).get("common", code)
                coords = p.get("latlng", [0, 0])
                borders = p.get("borders", [])

                grafo.adicionar_vertice(code, nome)
                paises_dict[code] = {
                    "nome": nome,
                    "coords": coords,
                    "borders": borders
                }

        # Popula as arestas (fronteiras)
        for code, info in paises_dict.items():
            for destino in info["borders"]:
                grafo.adicionar_aresta(code, destino)

        return paises_dict, grafo
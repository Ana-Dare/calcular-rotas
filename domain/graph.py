from collections import deque
from typing import Dict, List, Optional, Set

class GrafoPaises:
    def __init__(self):
        self.adjacencias: Dict[str, Set[str]] = {}
        self.nomes: Dict[str, str] = {}

    def adicionar_vertice(self, codigo: str, nome: str) -> None:
        if codigo not in self.adjacencias:
            self.adjacencias[codigo] = set()
            self.nomes[codigo] = nome

    def adicionar_aresta(self, codigo1: str, codigo2: str) -> None:
        if codigo1 in self.adjacencias and codigo2 in self.adjacencias:
            self.adjacencias[codigo1].add(codigo2)
            self.adjacencias[codigo2].add(codigo1)

    # Calcula o menor caminho em número de fronteiras
    def buscar_menor_caminho_bfs(self, inicio: str, fim: str) -> Optional[List[str]]:
        inicio, fim = inicio.upper(), fim.upper()

        if inicio not in self.adjacencias or fim not in self.adjacencias:
            return None

        fila = deque([[inicio]])
        visitados = {inicio}

        while fila:
            caminho = fila.popleft()
            no_atual = caminho[-1]

            if no_atual == fim:
                return caminho

            for vizinho in self.adjacencias[no_atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(caminho + [vizinho])

        return None
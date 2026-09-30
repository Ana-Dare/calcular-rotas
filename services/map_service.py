import folium
from config import MAPTILER_KEY

class MapService:

    def __init__(self, api_key: str = MAPTILER_KEY):
        self.api_key = api_key

    def gerar_mapa_rota(self, paises: dict, rota: list[str] = None, output_filename: str = "mapa_temp.html") -> None:
        tile_url = f"https://api.maptiler.com/maps/streets-v2/{{z}}/{{x}}/{{y}}.png?key={self.api_key}"
        attr = '&copy; <a href="https://www.maptiler.com/copyright/">MapTiler</a> &copy; OpenStreetMap'

        # Centraliza o mapa na origem da rota ou no centro do mundo 
        if rota and len(rota) > 0 and rota[0] in paises:
            coords_inicio = paises[rota[0]]["coords"]
            mapa = folium.Map(location=coords_inicio, zoom_start=3, tiles=tile_url, attr=attr)
        else:
            mapa = folium.Map(location=[20, 0], zoom_start=2, tiles=tile_url, attr=attr)

        # Desenha os marcadores e as linhas de conexão apenas se existir uma rota válida
        if rota:
            pontos_linha = []
            for code in rota:
                if code in paises:
                    info = paises[code]
                    coords = info["coords"]
                    pontos_linha.append(coords)

                    is_extremo = code in (rota[0], rota[-1])
                    folium.Marker(
                        location=coords,
                        popup=f"<b>{info['nome']}</b> ({code})",
                        icon=folium.Icon(color="red" if is_extremo else "blue")
                    ).add_to(mapa)

            if len(pontos_linha) > 1:
                folium.PolyLine(
                    locations=pontos_linha,
                    color="red",
                    weight=4,
                    opacity=0.8,
                    tooltip="Rota Terrestre (BFS)"
                ).add_to(mapa)

        mapa.save(output_filename)
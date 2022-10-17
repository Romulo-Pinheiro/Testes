from Destino import Destino

class DestinoRepository:
    lista_destino : Destino = []

    def __init__(self) -> None:
        pass

    def adicionar_destino(self, destino: Destino) -> None:
        self.lista_destino.append(destino)

    def checa_se_destino_existe(self, ddd: int) -> bool:
        for destino in self.lista_destino:
            if destino.ddd == ddd:
                return True
        return False

    def obter_destino_pelo_ddd(self, ddd: int) -> str:
        for destino in self.lista_destino:
            if destino.ddd == ddd:
                return destino.destino

    def __str__(self) -> str:
        formatText = "{0:<10} {1:<10} {2:<20}\n"
        menu = formatText.format("DDD", "|", "Destino")

        for destino in self.lista_destino:
            menu += formatText.format(destino.ddd, "|", destino.destino)
        return menu

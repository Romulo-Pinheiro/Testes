from DestinoRepository import DestinoRepository

class InterfaceUsuario:
    def __init__(self, destino_repository : DestinoRepository) -> None:
        self.destino_repository = destino_repository

    def solicitar_input_usuario(self) -> int:
        ddd_input = int(input('Informe um número inteiro que represente um DDD para descobrir o seu destino: '))
        return ddd_input

    def exibir_destino(self, ddd : int) -> str:
        return self.destino_repository.obter_destino_pelo_ddd(ddd)
    
    def saida_usuario(self) -> bool:
        ddd_input = self.solicitar_input_usuario()
        if not self.destino_repository.checa_se_destino_existe(ddd_input):
            print("DDD não cadastrado")
            return False
        print(self.exibir_destino(ddd_input))
        return True
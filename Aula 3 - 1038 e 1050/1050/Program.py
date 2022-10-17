from Destino import Destino
from DestinoRepository import DestinoRepository
from InterfaceUsuario import InterfaceUsuario

destino_repository = DestinoRepository()
destino_repository.adicionar_destino(Destino(61, 'Brasilia'))
destino_repository.adicionar_destino(Destino(71, 'Salvador'))
destino_repository.adicionar_destino(Destino(11, 'São Paulo'))
destino_repository.adicionar_destino(Destino(21, 'Rio de Janeiro'))
destino_repository.adicionar_destino(Destino(32, 'Juiz de Fora'))
destino_repository.adicionar_destino(Destino(19, 'Campinas'))
destino_repository.adicionar_destino(Destino(27, 'Vitória'))
destino_repository.adicionar_destino(Destino(31, 'Belo Horizonte'))
print(destino_repository)

interface_usuario = InterfaceUsuario(destino_repository)
while interface_usuario.saida_usuario():
    pass
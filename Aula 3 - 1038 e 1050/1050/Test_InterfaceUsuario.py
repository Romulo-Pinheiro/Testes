from InterfaceUsuario import DestinoRepository, InterfaceUsuario
from Destino import Destino

def test_exibir_destino():
    # Arrange
    destino_repository = DestinoRepository()
    destino1 = Destino(61, 'Brasilia')
    interface_usuario = InterfaceUsuario(destino_repository)

     # Act
    destino_repository.adicionar_destino(destino1)
    resultado_destino = interface_usuario.exibir_destino(61)
    destino_inexistente = interface_usuario.exibir_destino(1)

    # Assert
    assert resultado_destino == 'Brasilia'
    assert destino_inexistente == None

def test_solicitar_input_usuario(monkeypatch):
    # Arrange
    monkeypatch.setattr('builtins.input', lambda _: "61")
    destino_repository = DestinoRepository()
    interface_usuario = InterfaceUsuario(destino_repository)

    # Act
    valor = interface_usuario.solicitar_input_usuario()

    # Assert
    assert valor == 61

def test_saida_usuario(monkeypatch):
    # Arrange
    destino_repository = DestinoRepository()
    interface_usuario = InterfaceUsuario(destino_repository)
    destino1 = Destino(61, 'Brasilia')
    monkeypatch.setattr('builtins.input', lambda _: "61")

    # Act
    destino_repository.adicionar_destino(destino1)
    ddd_cadastrado = interface_usuario.saida_usuario()
    monkeypatch.setattr('builtins.input', lambda _: "1")
    ddd_nao_cadastrado = interface_usuario.saida_usuario()

    # Assert
    assert ddd_cadastrado == True
    assert ddd_nao_cadastrado == False
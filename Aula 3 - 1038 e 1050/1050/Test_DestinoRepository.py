from Destino import Destino
from DestinoRepository import DestinoRepository

def test_adicionar_destino():
    # Arrange
    destino_repository = DestinoRepository()
    destino1 = Destino(61, 'Brasilia')
    destino2 = Destino(71, 'Salvador')
    destino3 = Destino(11, 'São Paulo')
    destino4 = Destino(21, 'Rio de Janeiro')

    # Act
    destino_repository.adicionar_destino(destino1)
    destino_repository.adicionar_destino(destino2)  
    destino_repository.adicionar_destino(destino4)

    # Assert
    assert len(destino_repository.lista_destino) == 3
    assert not destino3 in destino_repository.lista_destino

def test_checa_se_destino_existe():
    # Arrange
    destino_repository = DestinoRepository()
    destino1 = Destino(61, 'Brasilia')
    destino2 = Destino(70, 'Teste')

    # Act
    destino_repository.adicionar_destino(destino1)

    # Assert
    assert destino_repository.checa_se_destino_existe(destino1.ddd) == True
    assert destino_repository.checa_se_destino_existe(destino2.ddd) == False

def test_obter_destino_pelo_ddd():
    # Arrange
    destino_repository = DestinoRepository()
    destino1 = Destino(61, 'Brasilia')

    # Act
    destino_repository.adicionar_destino(destino1)
    resultado_destino = destino_repository.obter_destino_pelo_ddd(61)
    destino_inexistente = destino_repository.obter_destino_pelo_ddd(1)
    
    # Assert
    assert resultado_destino == 'Brasilia'
    assert destino_inexistente == None

from datetime import datetime
from itertools import product

from Entities.Cliente import Cliente
from Entities.Pedido import Pedido
from Entities.PedidoProduto import PedidoProduto
from Entities.Produto import Produto
from Repositories.ClienteRepository import ClienteRepository
from Repositories.ProdutoRepository import ProdutoRepository


def test_new_order_with_product_total_price():
    # Arrange
    cliente = Cliente(1, "Jefté")
    cliente_repository = ClienteRepository()
    cliente_repository.adicionar_cliente(cliente)

    product1 = Produto(1, "Milk", 50, 10)
    product_repository = ProdutoRepository()
    product_repository.adicionar_produto(product1)

    pedido = Pedido(1, cliente, datetime.today)
    order_product1 = PedidoProduto()
    order_product1.adicionar_produto(product1, 5)
    pedido.adicionar_produto_pedido(order_product1)

    # Act
    pedido.atualizar_preco_total()

    # Assert
    assert pedido.valor_total == 250


def test_new_order_without_product():
    # Arrange
    cliente = Cliente(1, "Jefté")
    cliente_repository = ClienteRepository()
    cliente_repository.adicionar_cliente(cliente)

    product1 = Produto(1, "Milk", 50, 10)
    produto_repository = ProdutoRepository()
    produto_repository.adicionar_produto(product1)

    pedido = Pedido(1, cliente, datetime.today)
    pedido_produto = PedidoProduto()
    pedido_produto.adicionar_produto(product1, 15)
    pedido.adicionar_produto_pedido(pedido_produto)

    # Act
    pedido.atualizar_preco_total()

    # Assert
    assert pedido.valor_total == 0

def test_integrado_processar_produto():
    # Arrange
    cliente = Cliente(1, "Cliente Um")
    cliente_repository = ClienteRepository()
    cliente_repository.adicionar_cliente(cliente)

    product1 = Produto(1, "Chocolate", 15, 20)
    produto_repository = ProdutoRepository()
    produto_repository.adicionar_produto(product1)

    pedido = Pedido(1, cliente, datetime.today)
    pedido_produto = PedidoProduto()

    # Act
    pedido_produto.adicionar_produto(product1, 12)
    pedido.adicionar_produto_pedido(pedido_produto)

    # Assert
    assert pedido_produto.valor_item == 180


def test_integrado_baixar_estoque():
    # Arrange
    cliente = Cliente(1, "Cliente Um")
    cliente_repository = ClienteRepository()
    cliente_repository.adicionar_cliente(cliente)

    product1 = Produto(1, "Leite", 30, 12)
    produto_repository = ProdutoRepository()
    produto_repository.adicionar_produto(product1)

    pedido = Pedido(1, cliente, datetime.today)
    pedido_produto = PedidoProduto()


    # Act
    pedido_produto.adicionar_produto(product1, 9)
    estoque_insuficiente = pedido_produto.adicionar_produto(product1, 5)
    pedido.adicionar_produto_pedido(pedido_produto)


    # Assert
    assert product1.estoque == 3
    assert estoque_insuficiente == "Produto sem 'Leite' estoque."

def test_baixar_estoque():
    # Arrange
    product1 = Produto(1, "Pão", 30, 20)

    # Act
    product1.baixar_estoque(15)

    # Assert
    assert product1.estoque == 5
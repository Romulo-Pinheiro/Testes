from MenuRepository import MenuRepository, Menu, Order
from UserInterface import UserInterface

def test_get_total_price():
    # Arrange
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Test 1", 10)
    order1 = Order(1, 2)

    # Act
    menu_repository.set_menu_item(menu1)
    user_interface = UserInterface(menu_repository)
    total = user_interface.get_total_price(order1) 

    # Assert
    assert type(total) == int
    assert total == menu1.price * order1.quantity
    assert total >= 0
    
def test_get_user_input(monkeypatch):
    # Arrange
    menu_repository = MenuRepository()
    user_interface = UserInterface(menu_repository)
    menu1 = Menu(1, "Test 1", 6)
    monkeypatch.setattr('builtins.input', lambda _: "1 4")

    # Act
    menu_repository.set_menu_item(menu1)
    user_input = user_interface.get_user_input()

    # Assert
    assert type(user_input) == Order
    assert user_input.code == 1
    assert user_input.quantity == 4

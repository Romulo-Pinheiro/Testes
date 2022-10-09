from Coordinate import Coordinate
from Quadrant import Quadrant
from Menu import Menu

def test_quadrant_should_be_second():
    # Arrange / Setup
    a = -5
    b = 20
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Second"

def test_quadrant_should_be_third():
    # Arrange / Setup
    a = -5
    b = -15
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == "Third"


def test_not_valid_coordinate():
    # Arrange / Setup
    a = 0
    b = 12
    coordinates = Coordinate(a, b)
    menu = Menu()

    # Act / Action
    result = menu.cordinate_is_valid(coordinates)
    # Assert
    assert result == False

def test_empty_return():
    # Arrange / Setup
    a = 0
    b = 15
    coordinates = Coordinate(a, b)
    quadrant = Quadrant(coordinates)

    # Act / Action
    result = quadrant.get_quadrant_coordinate()
    # Assert
    assert result == ""
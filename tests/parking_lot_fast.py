import pytest
from parking_lot.car import Car
from parking_lot.parking_lot_fast import ParkingLotFast

@pytest.fixture
def parking_lot():
    return ParkingLotFast(size=5)

def test_park_car(parking_lot):
    car1 = Car("A1")
    car2 = Car("A2")
    car3 = Car("A3")

    spot1 = parking_lot.park(car1)
    assert spot1 == 0

    spot2 = parking_lot.park(car2)
    assert spot2 == 1

    spot3 = parking_lot.park(car3)
    assert spot3 == 2

    assert parking_lot.spots[spot1] == car1
    assert parking_lot.spots[spot2] == car2
    assert parking_lot.spots[spot3] == car3

def test_park_full(parking_lot):
    car1 = Car("A1")
    car2 = Car("A2")
    car3 = Car("A3")
    car4 = Car("A4")
    car5 = Car("A5")
    car6 = Car("A6")

    parking_lot.park(car1)
    parking_lot.park(car2)
    parking_lot.park(car3)
    parking_lot.park(car4)
    parking_lot.park(car5)

    # Try to park in a full parking lot
    result = parking_lot.park(car6)
    assert result == -1

def test_unpark_car(parking_lot):
    car1 = Car("A1")
    car2 = Car("A2")
    car3 = Car("A3")

    spot1 = parking_lot.park(car1)
    print(spot1)
    spot2 = parking_lot.park(car2)
    print(spot2)
    spot3 = parking_lot.park(car3)
    print(spot3)

    # Unpark the second car
    result = parking_lot.unpark(spot2)
    assert result == spot2
    assert parking_lot.spots[spot2] is None
    assert spot2 in parking_lot.empty_spots

def test_unpark_empty_spot(parking_lot):
    # Try to unpark an empty spot
    result = parking_lot.unpark(0)
    assert result == -1

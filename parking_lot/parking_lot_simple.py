from car import Car


class ParkingLot:
    def __init__(self, size) -> None:
        self.spots = [None] * size
        
    def park(self, car: Car) -> int:
        if self.spots.count(None) == 0:
            return -1
        idx = self.spots.index(None)
        self.spots[idx] = car
        return idx
        
    def unpark(self, id: int) -> int:
        if id < 0 or id > len(self.spots) - 1 or self.spots[id] == None:
            return -1
        self.spots[id] = None
        return id
from parking_lot.car import Car


class ParkingLotFast:
    def __init__(self, size) -> None:
        self.size = size
        self.spots = []
        self.empty_spots = []
        
    def park(self, car: Car) -> int:
        if len(self.spots) >= self.size:
            return -1
        elif len(self.empty_spots) > 0:
            spot = self.empty_spots[0]
            self.spots[spot] = car
            del self.empty_spots[0]
            return spot
        else:
            self.spots.append(car)
            return len(self.spots) - 1
        
    def unpark(self, id: int) -> int:
        if id >= len(self.spots) or self.spots[id] == None:
            return -1
        self.spots[id] = None
        self.empty_spots.append(id)
        return id
class ParkingSpot:
    def __init__(self):
        self.__is_occupied__: bool = False
        self.__vehicle_no__: str | None = None

    def park(self, vehicle_no: str) -> None:
        if self.__is_occupied__:
            raise ValueError('Cannot park in an occupied spot')
        if not vehicle_no or not vehicle_no.strip():
            raise ValueError('Cannot park without a vehicle number')

        self.__is_occupied__ = True
        self.__vehicle_no__ = vehicle_no

    def unpark(self) -> None:
        if not self.__is_occupied__:
            raise ValueError('Cannot unpark an empty spot')

        self.__is_occupied__ = False
        self.__vehicle_no__ = None

    def __str__(self) -> str:
        return 'Parking spot: ' + (f'[Occupied by {self.__vehicle_no__}]' if self.__is_occupied__ else '[Empty]')

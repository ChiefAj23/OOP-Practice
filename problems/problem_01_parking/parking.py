from datetime import datetime, timedelta
import math

class Vehicle:
    def __init__(self, plate:str, base_fee:float):
        self._plate = plate
        self._base_fee = base_fee

    @property
    def plate(self) -> str:
        return self._plate

    @property
    def base_fee(self) -> float:
        return self._base_fee

class Car(Vehicle):
    def __init__(self, plate:str):
        super().__init__(plate, base_fee=5.0)

class Bike(Vehicle):
    def __init__(self, plate:str):
        super().__init__(plate, base_fee=2.0)

class Ticket:
    def __init__(self, vehicle:Vehicle, entry_time:datetime):
        self._vehicle=vehicle
        self._entry_time=entry_time
        self._exit_time=None

    @property
    def vehicle(self) -> Vehicle:
        return self._vehicle
    @property
    def entry_time(self) -> datetime:
        return self._entry_time
    @property
    def exit_time(self) -> datetime | None:
        return self._exit_time

    def close(self, exit_time: datetime):
        self._exit_time = exit_time

    def total_fee(self) -> float:
        if self.exit_time is None:
            raise ValueError("Ticket is still open")
        hours = float((self._exit_time - self._entry_time).total_seconds()/3600)
        #print(f"Total hours parked: {hours}")
        round_hours = math.ceil(hours)
        #print(f"Total hours parked (rounded): {round_hours}")
        return self._vehicle.base_fee + (round_hours * 1)

class Gate:
    def issue_ticket(self,vehicle:Vehicle) -> Ticket:
        return Ticket(vehicle, entry_time= datetime.now())

if __name__ == "__main__":
    gate = Gate()
    # Car parks for 1.5 hours
    t1 = gate.issue_ticket(Car("CAR-111"))
    t1.close(t1.entry_time + timedelta(hours=1, minutes=30))
    print(f"Fee: {t1.total_fee()} | Plate: {t1.vehicle.plate}")

    # Bike parks for 3.5 hours
    t2 = gate.issue_ticket(Bike("BIKE-222"))
    t2.close(t2.entry_time + timedelta(hours=3, minutes=30))
    print(f"Fee: {t2.total_fee()} | Plate: {t2.vehicle.plate}")




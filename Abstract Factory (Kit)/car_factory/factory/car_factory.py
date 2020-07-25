from abc import ABC, abstractmethod
from car_models import CarModel
# from factory import toyota_factory, volvo_factory


class CarFactory(ABC):
    @abstractmethod
    def produce_body(self, model: CarModel):
        pass

    @abstractmethod
    def produce_wheels(self, model: CarModel):
        pass

    @abstractmethod
    def produce_interior(self, model: CarModel):
        pass

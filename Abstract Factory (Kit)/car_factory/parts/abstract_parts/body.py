from abc import (
    property,
    ABC
)


class Body(ABC):
    @property
    def weight(self):
        pass

    @property
    def material(self):
        pass

    @property
    def volume(self):
        pass

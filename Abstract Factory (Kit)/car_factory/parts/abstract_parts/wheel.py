from abc import (
    property,
    ABC
)


class Wheel(ABC):
    @property
    def width(self):
        pass

    @property
    def size(self):
        pass

    @property
    def type(self):
        pass

from abc import ABCMeta, abstractmethod


class Object(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def move(self, dx, dy):
        pass

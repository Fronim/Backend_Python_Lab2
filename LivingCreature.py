from abc import ABC, abstractmethod

class LivingCreature(ABC):

    @abstractmethod
    def get_fname(self):
        pass

    @abstractmethod
    def get_age(self):
        pass
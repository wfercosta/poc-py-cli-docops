
from abc import ABCMeta, abstractmethod

class ICommand:

    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self, arguments):
        pass
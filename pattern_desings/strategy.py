from abc import ABC, abstractmethod

class Operation(ABC):
    """
    Abstract class
    """

    @abstractmethod
    def calculate_the_operation(self, a, b):
        pass


class Addition(Operation):
    """
    strategy of addition
    """

    def calculate_the_operation(self, a, b):
        return a+b


class Sustration(Operation):
    """
    strategy of sustraction
    """

    def calculate_the_operation(self, a, b):
        return a-b



class OperationContext:


    def __init__(self, strategy: Operation) :
        self._strategy = strategy


    def set_strategy(self, strategy: Operation) :
        self._strategy = strategy

    def calculate_the_operation(self, a, b):

        return self._strategy.calculate_the_operation(a, b)



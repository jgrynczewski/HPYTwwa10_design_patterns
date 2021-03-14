import abc


class IAdapter(abc.ABC):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    @property
    def adaptee(self):
        return self._adaptee

    @property
    @abc.abstractmethod
    def name(self):
        pass

    @property
    @abc.abstractmethod
    def address(self):
        pass

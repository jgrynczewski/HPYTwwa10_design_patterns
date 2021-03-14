#ISP

# łamiemy

class IMachine:
    def print(self, document):
        raise NotImplemented

    def fax(self, document):
        raise NotImplemented

    def scan(self, document):
        raise NotImplemented


class MultiFunctionalPrinter(IMachine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(IMachine):
    def print(self, document):
        print("OK")

# Nie łamiemy ISP

import abc


class IPrinter:
    @abc.abstractmethod
    def print(self, document):
        pass


class IScan:
    @abc.abstractmethod
    def scan(self, document):
        pass


class IFax:
    @abc.abstractmethod
    def fax(self, document):
        pass


class OldFashionedPrinter(IPrinter):
    def print(self, document):
        print("ok")


class PhotoCopier(IPrinter, IScan):
    def print(self, document):
        print("ok")

    def scan(self, document):
        print("ok")


class IMulitFunctionalDevice(IPrinter, IScan, IFax):
    pass


class MultiFunctionalDevice(IMulitFunctionalDevice):
    def print(self, document):
        print("ok")

    def scan(self, document):
        print("ok")

    def fax(self, document):
        print("ok")

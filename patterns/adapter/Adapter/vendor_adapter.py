from iadapter import IAdapter


class VendorAdapter(IAdapter):
    @property
    def name(self):
        return self.adaptee.name

    @property
    def address(self):
        return f"{self.adaptee.street} {self.adaptee.number}"
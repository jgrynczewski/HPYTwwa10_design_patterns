# Dziedziczenie
# DRY

class UIControl:
    def enable(self):
        print("Enable")


class TextBox(UIControl):
    pass

t = TextBox().enable()

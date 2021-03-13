# Polimorfizm - wielopostaciowość
import abc


class UIControl(abc.ABC):
    def enable(self):
        print("Enable")

    @abc.abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Drawing a textbox")


class CheckBox(UIControl):
    def draw(self):
        print("Drawing a checkbox")


def draw_ui_control(ui_control: UIControl):
    ui_control.draw()


draw_ui_control(TextBox())
draw_ui_control(CheckBox())

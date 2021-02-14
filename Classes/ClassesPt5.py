from abc import ABC, abstractmethod


class UIControl(ABC):

    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("textbox draw")


class DropDownList(UIControl):
    def draw(self):
        print("dropdownlist draw")


def draw(controls):
    for control in controls:
        control.draw()

ddl = DropDownList()
textbox = TextBox()

draw([ddl, textbox])


import idom
from .idom_loader import load_component


class Widget:

    def __init__(self):
        self.__widget = load_component(name='Widget')

    @idom.component
    def show(self):
        return self.__widget()
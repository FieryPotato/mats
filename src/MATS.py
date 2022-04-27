from src.Writer import Writer
from src.io import IOManager


class Mats:
    def __init__(self):
        self.data = IOManager().load()

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delattr__(self, item):
        del self.data[item]

    def add_item(self):
        keys = Writer().get_keys()
        value = Writer().get_value()
        remaining_keys = keys[::-1]
        total = {remaining_keys.pop(0): value}
        for k in remaining_keys:
            total = {k: total}
        self.data.update(total)


MATS = Mats()

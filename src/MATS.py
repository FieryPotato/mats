from collections.abc import MutableMapping
from typing import Iterator

from src.Writer import Writer
from src.io import IOManager


class _MATS(MutableMapping):
    def __iter__(self) -> Iterator['_T_co']:
        yield from self.data.__iter__()

    def __len__(self) -> int:
        return self.data.__len__()

    def __delitem__(self, v: '_KT') -> None:
        del self.data[v]

    def __init__(self):
        self.data = IOManager().load()

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def add_item(self):
        keys = Writer().get_keys()
        value = Writer().get_value()
        remaining_keys = keys[::-1]
        total = {remaining_keys.pop(0): value}
        for k in remaining_keys:
            total = {k: total}
        self.data.update(total)

    def save(self):
        IOManager().save(self.data)


sentinel = None


def MATS():
    global sentinel
    if sentinel is None:
        sentinel = _MATS()
    return sentinel

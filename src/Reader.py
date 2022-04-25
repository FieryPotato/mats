from src.io import IOManager


class Reader:
    def __init__(self):
        self.mats = IOManager().load()

    def full_path_find(self, item, *further_items):
        if not further_items:
            return self.mats[item]
        keys = [k for k in further_items[::-1]]
        current = self.mats[item]
        while keys:
            current = current[keys.pop()]
        return current
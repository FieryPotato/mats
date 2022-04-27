from src.MATS import MATS


class _Reader:
    def __init__(self):
        self.mats = MATS()

    def full_path_find(self, item, *further_items):
        try:
            if not further_items:
                return self.mats[item]
            keys = [k for k in further_items[::-1]]
            current = self.mats[item]
            while keys:
                current = current[keys.pop()]
            return current
        except KeyError:
            if not further_items:
                return [path for path in self.deep_search(item)]

    def deep_search(self, item, sub_mats=None):
        if sub_mats is None:
            sub_mats = self.mats
        for key, value in sub_mats.items():
            if isinstance(value, dict):
                for path in self.deep_search(item, sub_mats=value):
                    if key == item or item in path:
                        yield key, *path
            else:
                if key == item or value == item:
                    yield key, value


def pathify(path):
    full_path = ['MATS']
    full_path.extend(path)
    return ' > '.join(full_path)


sentinel = None


def Reader() -> _Reader:
    global sentinel
    if sentinel is None:
        sentinel = _Reader()
    return sentinel

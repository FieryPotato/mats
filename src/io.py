import json


class _IOManager:
    path: str = 'data/MATS.json'

    def load(self) -> dict:
        with open(self.path) as file:
            return json.load(file)

    def save(self, data: dict) -> None:
        with open(self.path, 'w') as file:
            json.dump(data, file)

    def multi_input(self, prompt='') -> str:
        input_list = [None]
        print(prompt)
        while input_list[-1] != '':
            input_list.append(input())
        return "\n".join(input_list[1:-1])




sentinel = None


def IOManager() -> _IOManager:
    """
    Singleton object containing i/o functions for this program.

    :return: _IOManager object
    """

    global sentinel
    if sentinel is None:
        sentinel = _IOManager()
    return sentinel

import json


class _IOManager:
    mats_path: str = 'data/MATS.json'

    def load(self) -> dict:
        with open(self.mats_path) as file:
            return json.load(file)

    def save(self, data: dict) -> None:
        with open(self.mats_path, 'w') as file:
            json.dump(data, file)

    def multi_input(self, prompt='') -> str:
        input_list = [None]
        while input_list[-1] != '':
            print(prompt)
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

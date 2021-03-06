from src.io import IOManager


class Writer:
    def get_keys(self):
        prompt = "Enter keys in order individually or in a comma-separated list."
        keys = IOManager().multi_input(prompt)
        splitters = [',', '\n']
        strippers = ' '
        for character in splitters:
            if character in keys:
                return [word.strip(strippers)
                        for word in keys.split(character)]

    def get_value(self):
        prompt = "Enter value. Line breaks will be ignored."
        value = IOManager().multi_input(prompt)
        return value.replace('\n', ' ')

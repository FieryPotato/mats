import json
import os
import unittest
from unittest.mock import patch, PropertyMock

from src.io import IOManager


class TestLoad(unittest.TestCase):

    def test_loader_target_file(self):
        path = 'data/MATS.json'
        self.assertEqual(path, IOManager().path)

    def test_loader_opens_json(self):
        data = {'key', 'value'}
        with patch('json.load', return_value=data):
            self.assertEqual(data, IOManager().load())


class TestSave(unittest.TestCase):
    def test_save_mats(self):
        data = {'key': 'value'}
        with file_write_cm() as cm:
            with patch('src.io._IOManager.path', new_callable=PropertyMock) as mock:
                mock.return_value = cm.path
                IOManager().save(data)
                with open(cm.path) as file:
                    self.assertEqual(data, json.load(file))


class TestInput(unittest.TestCase):
    def test_get_input(self):
        input_list = ["one", "two", "three", ""]
        expected = "\n".join(input_list[:-1])
        with patch("builtins.input", side_effect=input_list):
            data = IOManager().multi_input()
            self.assertEqual(expected, data)


class file_write_cm:
    path = 'test\\test_write.json'

    def __enter__(self):
        f = open(self.path, 'w')
        f.write('{}')
        f.close()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.path)


if __name__ == '__main__':
    unittest.main()

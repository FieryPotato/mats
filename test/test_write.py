import os
import unittest
from unittest import mock

from src.Writer import Writer
from src.io import _IOManager


class TestWriter(unittest.TestCase):
    path = 'test/MATS.json'

    def setUp(self) -> None:
        open(self.path, 'x').close()
        self.old_path = _IOManager.path
        _IOManager.path = self.path

    def tearDown(self) -> None:
        os.remove(self.path)
        _IOManager.path = self.old_path

    def test_ask_for_keys_as_multi_input(self):
        expected = ['a', 'b', 'c']
        inputs = ['a', 'b', 'c', '']
        with mock.patch('builtins.input', side_effect=inputs):
            keys = Writer().get_keys()
        self.assertEqual(expected, keys)

    def test_ask_for_keys_as_comma_separated_list(self):
        expected = ['a', 'b', 'c']
        inputs = ['a, b, c', '']
        with mock.patch('builtins.input', side_effect=inputs):
            keys = Writer().get_keys()
        self.assertEqual(expected, keys)


if __name__ == '__main__':
    unittest.main()
